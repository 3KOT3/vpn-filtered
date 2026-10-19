"""Публикация результата проверки боту (для российского VPS).

Запускается после check.py: берёт готовые файлы и отправляет их воркеру —
список попадает в подписку, статус обновляет главный экран бота.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

APP_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("OUT_DIR") or os.path.join(APP_DIR, "out")

WORKER_URL = (os.environ.get("WORKER_URL") or "").rstrip("/")
CHECKER_KEY = os.environ.get("CHECKER_KEY") or ""
PUBLISH_KEY = os.environ.get("PUBLISH_KEY") or "pub-7Qm2xVp9LzR4tNb8sWk3"


def log(message: str) -> None:
    print(message, flush=True)


def read(name: str) -> str:
    path = os.path.join(OUT_DIR, name)
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return ""


def post(path: str, payload: dict, timeout: int = 90) -> tuple:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(WORKER_URL + path, data=data, method="POST")
    request.add_header("content-type", "application/json; charset=utf-8")
    request.add_header("user-agent", "vpn-checker-vm")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", "replace")[:200]
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")[:200]
    except Exception as exc:  # noqa: BLE001
        return 0, f"{type(exc).__name__}: {exc}"


def main() -> int:
    if not WORKER_URL:
        log("WORKER_URL не задан — публиковать некуда")
        return 1

    plain = read("1.txt").strip()
    if not plain:
        log("список пуст — не публикую (старый остаётся у бота)")
        return 0

    auto = read("auto-legacy.json").strip()
    status_raw = read("status.json")
    history_raw = read("history.json")

    kept = len([line for line in plain.splitlines() if line.strip()])
    log(f"публикую {kept} конфигов")

    code, body = post(
        f"/publish?quiet=1&key={urllib.parse.quote(CHECKER_KEY)}",
        {"plain": plain + "\n", "auto": auto, "status": status_raw},
    )
    log(f"  список -> HTTP {code} {body}")

    try:
        status_obj = json.loads(status_raw or "{}")
    except ValueError:
        status_obj = {}
    try:
        history_obj = json.loads(history_raw or "[]")
    except ValueError:
        history_obj = []
    if status_obj:
        code, body = post(
            f"/publish-status?key={urllib.parse.quote(PUBLISH_KEY)}",
            {"status": status_obj, "history": history_obj},
        )
        log(f"  статус -> HTTP {code} {body}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
