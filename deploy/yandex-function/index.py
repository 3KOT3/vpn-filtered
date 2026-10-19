"""Проверка VPN-конфигов ИЗ РОССИИ в Yandex Cloud Functions.

Функция делает ровно то же, что домашний check.bat: гоняет конфиги через
sing-box (YouTube → Telegram → дата-центр Telegram → скорость) и публикует
результат боту. Главное отличие — она живёт в российском дата-центре и работает
даже когда компьютер выключен.

Переменные окружения (задаются при создании версии в консоли):
    WORKER_URL    — адрес воркера бота
    CHECKER_KEY   — секрет публикации списка (пишет подписку)
    PUBLISH_KEY   — открытый ключ публикации статуса
    MIN_MBPS      — порог скорости, по умолчанию 1.0
    SOURCES       — какие файлы проверять, например "6,22,23"
"""

import json
import os
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request

SING_BOX_VERSION = os.environ.get("SING_BOX_VERSION", "1.14.3")
WORKER_URL = (os.environ.get("WORKER_URL") or "").rstrip("/")
CHECKER_KEY = os.environ.get("CHECKER_KEY", "")
PUBLISH_KEY = os.environ.get("PUBLISH_KEY", "")
MIN_MBPS = os.environ.get("MIN_MBPS", "1.0")
SOURCES = os.environ.get("SOURCES", "6,22,23")

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
TMP = "/tmp"
SING_BOX_PATH = os.path.join(TMP, "sing-box")


def log(message: str) -> None:
    print(message, flush=True)


def ensure_sing_box() -> str:
    """Скачивает sing-box в /tmp один раз на тёплый экземпляр функции."""
    if os.path.exists(SING_BOX_PATH):
        return SING_BOX_PATH
    url = (
        f"https://github.com/SagerNet/sing-box/releases/download/v{SING_BOX_VERSION}/"
        f"sing-box-{SING_BOX_VERSION}-linux-amd64.tar.gz"
    )
    archive = os.path.join(TMP, "sing-box.tar.gz")
    log(f"скачиваю sing-box {SING_BOX_VERSION}")
    request = urllib.request.Request(url, headers={"User-Agent": "vpn-checker-function"})
    with urllib.request.urlopen(request, timeout=120) as response, open(archive, "wb") as handle:
        handle.write(response.read())
    with tarfile.open(archive) as tar:
        tar.extractall(TMP)
    source = os.path.join(TMP, f"sing-box-{SING_BOX_VERSION}-linux-amd64", "sing-box")
    os.replace(source, SING_BOX_PATH)
    os.chmod(SING_BOX_PATH, 0o755)
    return SING_BOX_PATH


def post_json(path: str, payload: dict, timeout: int = 90) -> tuple:
    if not WORKER_URL:
        return 0, "WORKER_URL не задан"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(WORKER_URL + path, data=data, method="POST")
    request.add_header("content-type", "application/json; charset=utf-8")
    request.add_header("user-agent", "vpn-checker-function")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", "replace")[:200]
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")[:200]
    except Exception as exc:  # noqa: BLE001
        return 0, f"{type(exc).__name__}: {exc}"


def read_text(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return ""


def handler(event, context):  # noqa: ARG001
    started = time.time()
    sing_box = ensure_sing_box()

    out_dir = os.path.join(TMP, "out")
    cmd = [
        sys.executable,
        os.path.join(CODE_DIR, "checker", "check.py"),
        "--sing-box", sing_box,
        "--out-dir", out_dir,
        "--work-dir", os.path.join(TMP, "work"),
        "--cache-dir", os.path.join(TMP, "sources"),
        "--min-mbps", MIN_MBPS,
        "--min-keep", "1",
        "--source-files", SOURCES,
    ]
    log("запуск проверки: " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=CODE_DIR)
    duration = round(time.time() - started, 1)

    if result.returncode != 0:
        log(f"check.py вернул код {result.returncode}")
        # 3 — слишком мало рабочих: старый список не трогаем
        return {"statusCode": 200, "body": json.dumps({"ok": False, "code": result.returncode})}

    plain = read_text(os.path.join(out_dir, "1.txt")).strip()
    auto = read_text(os.path.join(out_dir, "auto-legacy.json")).strip()
    status_raw = read_text(os.path.join(out_dir, "status.json"))
    history_raw = read_text(os.path.join(out_dir, "history.json"))

    kept = len([line for line in plain.splitlines() if line.strip()])
    log(f"проверка закончена за {duration} с, в списке {kept}")

    published = {}
    if plain:
        # подписка: кладёт список и конфиг в KV бота
        published["subscription"] = post_json(
            f"/publish?quiet=1&key={urllib.parse.quote(CHECKER_KEY)}",
            {"plain": plain + "\n", "auto": auto, "status": status_raw},
        )
        # статус: бот обновляет главный экран без нового сообщения
        if PUBLISH_KEY:
            try:
                status_obj = json.loads(status_raw or "{}")
            except ValueError:
                status_obj = {}
            try:
                history_obj = json.loads(history_raw or "[]")
            except ValueError:
                history_obj = []
            published["status"] = post_json(
                f"/publish-status?key={urllib.parse.quote(PUBLISH_KEY)}",
                {"status": status_obj, "history": history_obj},
            )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"ok": True, "kept": kept, "duration_sec": duration, "published": published},
            ensure_ascii=False,
        ),
    }
