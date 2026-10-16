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
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
CONFIG_PATH = os.path.join(HERE, "config.local.json")
WORK_DIR = os.path.join(HERE, ".work")


def log(message: str = "") -> None:
    print(message, flush=True)


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


def run_checker(config: dict, sing_box: str) -> str:
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
    sources = config.get("sources")
    if sources:
        cmd += ["--source-files", ",".join(str(item) for item in sources)]
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
    status["files"] = {"plain": "local.txt", "base64": "local-base64.txt"}
    status["link_plain"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local.txt"
    status["link_base64"] = f"https://github.com/{repo}/raw/refs/heads/{branch}/local-base64.txt"

    payloads = {
        "local.txt": open(os.path.join(out_dir, "1.txt"), "rb").read(),
        "local-base64.txt": open(os.path.join(out_dir, "1-base64.txt"), "rb").read(),
        "local-status.json": (json.dumps(status, ensure_ascii=False, indent=2) + "\n").encode(),
    }

    pushed = {}
    for name, raw in payloads.items():
        existing = github_call(config, "GET", f"/repos/{repo}/contents/{name}?ref={branch}")
        body = {
            "message": f"Локальная проверка: {status['counts']['kept']} рабочих конфигов",
            "content": base64.b64encode(raw).decode("ascii"),
            "branch": branch,
        }
        if existing[0] == 200 and isinstance(existing[1], dict):
            body["sha"] = existing[1].get("sha")
        code, response = github_call(config, "PUT", f"/repos/{repo}/contents/{name}", body)
        if code not in (200, 201):
            message = response.get("message") if isinstance(response, dict) else response
            log(f"  не удалось загрузить {name}: HTTP {code} {message}")
            raise SystemExit(1)
        pushed[name] = (response.get("commit") or {}).get("sha", "")[:8]
        log(f"  загружено {name}")
    return {"status": status, "pushed": pushed}


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
    out_dir = run_checker(config, sing_box)
    result = publish(config, out_dir)
    status = result["status"]

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
