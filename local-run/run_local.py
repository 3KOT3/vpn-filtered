#!/usr/bin/env python3
"""Проверка VPN-конфигов ИЗ ВАШЕЙ СЕТИ и публикация результата.

Зачем это отдельно от GitHub Actions: раннеры GitHub стоят в США/Европе, и
прокси, который прекрасно работает оттуда, может быть заблокирован РКН у вас.
Знать, что доступно именно из вашего интернета, можно только проверяя из него.

Скрипт:
  1. скачивает исходный список конфигов;
  2. гоняет каждый через sing-box ровно теми же проверками, что и CI
     (YouTube, Telegram, дата-центр Telegram, скорость);
  3. кладёт результат в репозиторий как local.txt / local-base64.txt /
     local-status.json, чтобы бот мог его отдать.

Настройки — в config.local.json рядом со скриптом (в репозиторий не попадает).
"""

from __future__ import annotations

import base64
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
CONFIG_PATH = os.path.join(HERE, "config.local.json")
WORK_DIR = os.path.join(HERE, ".work")


def log(message: str = "") -> None:
    print(message, flush=True)


LOCK_PATH = os.path.join(HERE, ".work", "run.lock")
LOCK_TTL_SEC = 900


def acquire_lock() -> bool:
    """Не даёт двум проверкам идти одновременно (задача + ручной запуск)."""
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    if os.path.exists(LOCK_PATH):
        age = time.time() - os.path.getmtime(LOCK_PATH)
        if age < LOCK_TTL_SEC:
            return False
    with open(LOCK_PATH, "w", encoding="utf-8") as handle:
        handle.write(str(os.getpid()))
    return True


def release_lock() -> None:
    try:
        os.remove(LOCK_PATH)
    except OSError:
        pass

def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        log(f"Нет файла настроек: {CONFIG_PATH}")
        log("Скопируйте config.local.example.json в config.local.json и впишите токен.")
        sys.exit(1)
    with open(CONFIG_PATH, encoding="utf-8") as handle:
        config = json.load(handle)
    if not config.get("github_token"):
        log("В config.local.json не заполнен github_token.")
        sys.exit(1)
    return config


def find_sing_box(config: dict) -> str:
    candidates = [
        config.get("sing_box"),
        os.path.join(HERE, "sing-box.exe"),
        os.path.join(HERE, "sing-box"),
        os.path.join(REPO_ROOT, ".cache", "sing-box", "sing-box.exe"),
        "sing-box",
    ]
    for candidate in candidates:
        if not candidate:
            continue
        if os.path.sep in candidate or candidate.endswith(".exe"):
            if os.path.exists(candidate):
                return os.path.abspath(candidate)
        else:
            from shutil import which

            found = which(candidate)
            if found:
                return found
    log("Не найден sing-box.")
    log("Скачайте его с https://github.com/SagerNet/sing-box/releases (windows-amd64),")
    log("распакуйте и укажите путь в config.local.json -> sing_box")
    sys.exit(1)


def fetch_bot_sources(config: dict):
    """Спрашивает у бота, какие источники сейчас включены.

    Так домашняя проверка идёт по тем же источникам, что и облачная: если в
    боте включены авто-источники — ПК проверяет их же, но из сети владельца.
    """
    base = str(config.get("worker_url") or "").rstrip("/")
    key = str(config.get("publish_key") or "")
    if not base or not key:
        return None
    try:
        request = urllib.request.Request(
            f"{base}/checker-sources?key={urllib.parse.quote(key)}",
            headers={"user-agent": "vpn-filtered-local"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read() or b"{}")
        sources = [str(item) for item in (data.get("sources") or []) if str(item).strip()]
        log(f"источники из бота: {len(sources)}")
        return sources or None
    except Exception as exc:  # noqa: BLE001
        log(f"  источники у бота не получены: {type(exc).__name__}: {exc}")
        return None

def fetch_cloud_list(config: dict) -> str:
    """Скачивает готовый список из облака — его и будем пинговать с ПК.

    Читаем через Contents API, а не raw.githubusercontent: тот кэширует файл
    до 5 минут и можно пинговать вчерашний список.
    """
    repo = config.get("repo", "3KOT3/vpn-filtered")
    branch = config.get("branch", "main")
    url = f"https://api.github.com/repos/{repo}/contents/1.txt?ref={branch}"
    request = urllib.request.Request(url, headers={"User-Agent": "vpn-filtered-local"})
    request.add_header("Accept", "application/vnd.github.raw")
    token = str(config.get("github_token") or "")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=60) as response:
        text = response.read().decode("utf-8", "replace")
    directory = os.path.join(WORK_DIR, "cloud-src")
    os.makedirs(directory, exist_ok=True)
    for name in os.listdir(directory):
        if name.endswith(".txt"):
            os.remove(os.path.join(directory, name))
    with open(os.path.join(directory, "cloud.txt"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    count = len([line for line in text.splitlines() if line.strip()])
    log(f"Облачный список: {count} конфигов — пингуем их с вашего ПК")
    return directory


def run_checker(config: dict, sing_box: str, sources_dir: str = None) -> str:
    out_dir = os.path.join(WORK_DIR, "out")
    cmd = [
        sys.executable,
        os.path.join(REPO_ROOT, "checker", "check.py"),
        "--out-dir", out_dir,
        "--work-dir", os.path.join(WORK_DIR, "singbox"),
        "--cache-dir", os.path.join(WORK_DIR, "sources"),
        "--sing-box", sing_box,
        "--min-mbps", str(config.get("min_mbps", 2.0)),
    ]
    if sources_dir:
        cmd += ["--sources-dir", sources_dir]
    else:
        sources = config.get("sources")
        if sources:
            cmd += ["--source-files", ",".join(str(item) for item in sources)]
    if config.get("delay_timeout_ms"):
        cmd += ["--delay-timeout", str(config["delay_timeout_ms"])]
    if config.get("max_youtube_ms"):
        cmd += ["--max-youtube-ms", str(config["max_youtube_ms"])]
    if config.get("max_telegram_ms"):
        cmd += ["--max-telegram-ms", str(config["max_telegram_ms"])]
    if config.get("core_check"):
        # финальная проверка реальным HTTP-запросом: отсекает конфиги,
        # которые отвечают на пинг, но не тянут настоящую страницу
        cmd += ["--core-check"]
    if config.get("confirm"):
        cmd += ["--confirm"]
    # прогресс уходит прямо в бот: он будет рисовать полосу загрузки
    if config.get("worker_url"):
        cmd += [
            "--progress-url", config["worker_url"].rstrip("/") + "/progress",
            "--progress-key", str(config.get("worker_key", "")),
        ]
    log("Запускаю проверку: " + " ".join(cmd[:2]))
    log("")
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    if result.returncode != 0:
        log("")
        log(f"Проверка завершилась с кодом {result.returncode}.")
        log("Коды: 1 — нечего проверять, 3 — слишком мало рабочих конфигов,")
        log("      4 — сработала защита (в списке оказался конфиг без YouTube/Telegram).")
        sys.exit(result.returncode)
    return out_dir


def github_call(config: dict, method: str, path: str, payload=None):
    url = "https://api.github.com" + path
    data = json.dumps(payload).encode() if payload is not None else None
    last = None
    for attempt in range(3):
        request = urllib.request.Request(url, data=data, method=method)
        request.add_header("Authorization", f"Bearer {config['github_token']}")
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("User-Agent", "vpn-local-check")
        if data:
            request.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.status, json.loads(response.read() or b"{}")
        except urllib.error.HTTPError as exc:
            body = exc.read()
            try:
                return exc.code, json.loads(body)
            except Exception:
                return exc.code, body.decode("utf-8", "replace")[:300]
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2 + attempt * 2)
    raise RuntimeError(f"{method} {path}: {last}")


def publish(config: dict, out_dir: str) -> dict:
    repo = config.get("repo", "3KOT3/vpn-filtered")
    branch = config.get("branch", "main")

    with open(os.path.join(out_dir, "status.json"), encoding="utf-8") as handle:
        status = json.load(handle)
    status["vantage"] = "local"
    status["vantage_host"] = socket.gethostname()
    status["vantage_checked_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    status["files"] = {
        "plain": "local.txt",
        "base64": "local-base64.txt",
        "auto": "local-auto.json",
        "auto_yaml": "local-auto.yaml",
        "auto_legacy": "local-auto-legacy.json",
    }
    status["link_plain"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local.txt"
    status["link_base64"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local-base64.txt"
    status["link_auto"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local-auto.json"
    status["link_auto_yaml"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local-auto.yaml"

    payloads = {
        "local.txt": open(os.path.join(out_dir, "1.txt"), "rb").read(),
        "local-base64.txt": open(os.path.join(out_dir, "1-base64.txt"), "rb").read(),
        "local-auto.json": open(os.path.join(out_dir, "auto.json"), "rb").read(),
        "local-auto.yaml": open(os.path.join(out_dir, "auto.yaml"), "rb").read(),
        "local-auto-legacy.json": open(os.path.join(out_dir, "auto-legacy.json"), "rb").read(),
        "local-auto-client.json": open(os.path.join(out_dir, "auto-client.json"), "rb").read(),
        "local-status.json": (json.dumps(status, ensure_ascii=False, indent=2) + "\n").encode(),
    }

    pushed = {}
    for name, raw in payloads.items():
        body_message = f"Локальная проверка: {status['counts']['kept']} рабочих конфигов"
        for attempt in range(4):
            existing = github_call(config, "GET", f"/repos/{repo}/contents/{name}?ref={branch}")
            body = {
                "message": body_message,
                "content": base64.b64encode(raw).decode("ascii"),
                "branch": branch,
            }
            if existing[0] == 200 and isinstance(existing[1], dict):
                body["sha"] = existing[1].get("sha")
            code, response = github_call(config, "PUT", f"/repos/{repo}/contents/{name}", body)
            if code in (200, 201):
                break
            message = response.get("message") if isinstance(response, dict) else response
            if code == 409:
                # файл успели изменить между чтением и записью — перечитываем и повторяем
                log(f"  {name}: конфликт версий, повторяю ({attempt + 1}/4)")
                time.sleep(2 + attempt * 2)
                continue
            log(f"  не удалось загрузить {name}: HTTP {code} {message}")
            raise SystemExit(1)
        else:
            log(f"  не удалось загрузить {name}: постоянно конфликтует версия")
            raise SystemExit(1)
        pushed[name] = (response.get("commit") or {}).get("sha", "")[:8]
        log(f"  загружено {name}")
    return {"status": status, "pushed": pushed}


def publish_ru(config: dict, out_dir: str) -> None:
    """Отправляет проверенные ИЗ РОССИИ конфиги боту (в KV).

    Именно этот список потом использует облачная проверка: она берёт только
    те конфиги, которые реально открылись с домашнего подключения.
    """
    base = str(config.get("worker_url") or "").rstrip("/")
    key = str(config.get("publish_key") or "")
    if not base or not key:
        log("  список для CI не отправлен: нет worker_url / publish_key")
        return
    path = os.path.join(out_dir, "1.txt")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as handle:
        uris = [line.strip() for line in handle if line.strip()]
    if not uris:
        return
    request = urllib.request.Request(
        f"{base}/publish-ru?key={urllib.parse.quote(key)}",
        data=json.dumps({"uris": uris}, ensure_ascii=False).encode("utf-8"),
        method="POST",
    )
    request.add_header("content-type", "application/json; charset=utf-8")
    request.add_header("user-agent", "vpn-filtered-local")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read() or b"{}")
        log(f"  проверено из России: {len(uris)} конфигов -> бот (всего в снимке {payload.get('kept')})")
    except Exception as exc:  # noqa: BLE001
        log(f"  список для CI не отправился: {type(exc).__name__}: {exc}")

def notify_worker(config: dict) -> None:
    """Сказать боту, что список обновился.

    Без этого шага бот узнаёт о новой проверке только когда кто-нибудь напишет
    ему сам — именно поэтому новые списки раньше не приходили.
    """
    base = str(config.get("worker_url") or "").rstrip("/")
    key = str(config.get("worker_key") or "")
    if not base or not key:
        log("  бот не уведомлён: в config.local.json нет worker_url / worker_key")
        return
    url = f"{base}/notify?key={urllib.parse.quote(key)}"
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "vpn-local-check"})
        with urllib.request.urlopen(request, timeout=120) as response:
            answer = response.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(answer)
            log(f"  бот уведомлён: разослано {parsed.get('sent', 0)}, "
                f"пропущено {parsed.get('skipped', '—')}")
        except Exception:
            log(f"  бот уведомлён: {answer[:120]}")
    except Exception as exc:  # noqa: BLE001
        log(f"  бот не уведомлён: {type(exc).__name__}: {exc}")


def main() -> int:
    config = load_config()
    sing_box = find_sing_box(config)

    log("=" * 62)
    log("Проверка VPN-конфигов из вашей сети")
    log("=" * 62)
    log(f"sing-box: {sing_box}")
    log(f"порог скорости: {config.get('min_mbps', 2.0)} Мбит/с")
    log("")

    started = time.time()
    bot_sources = fetch_bot_sources(config) if config.get("use_bot_sources") else None
    if bot_sources:
        config = dict(config)
        config["sources"] = bot_sources
        sources_dir = None
    else:
        sources_dir = fetch_cloud_list(config) if config.get("ping_cloud_list") else None
    out_dir = run_checker(config, sing_box, sources_dir)
    result = publish(config, out_dir)
    status = result["status"]
    publish_ru(config, out_dir)
    notify_worker(config)

    log("")
    log("=" * 62)
    log(f"Готово за {time.time() - started:.0f} с")
    log(f"В списке: {status['counts']['kept']} конфигов из {status['counts']['unique']}")
    log(f"  прошли YouTube: {status['counts']['youtube_ok']}")
    log(f"  из них Telegram: {status['counts']['telegram_ok']}")
    log(f"  из них по скорости: {status['counts']['speed_ok']}")
    log("")
    log("Ссылка для v2rayNG / v2Box (обновляется после каждого запуска):")
    log(f"  {status['link_plain']}")
    log("")
    log("Откройте бота и нажмите «📶 Из вашей сети» — там та же ссылка.")
    log("=" * 62)
    return 0


if __name__ == "__main__":
    sys.exit(main())
