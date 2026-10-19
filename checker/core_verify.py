"""Финальная проверка конфигов реальным HTTP-запросом через туннель.

Проверка «пингом» (Clash API delay) показывает, что прокси ответил на один
запрос. Но клиент ходит иначе: он открывает соединение и тянет страницу.
Бывает, что пинг проходит, а реальный запрос отдаёт 502 — такой конфиг в
списке бесполезен.

Здесь для каждого конфига поднимается sing-box с HTTP-прокси на локальном
порту и через него запрашиваются YouTube и Telegram — ровно то, что делает
браузер после подключения.
"""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import uris  # noqa: E402

YOUTUBE_URL = "http://www.youtube.com/generate_204"
YOUTUBE_CODE = 204
TELEGRAM_URL = "https://core.telegram.org/"
TELEGRAM_CODE = 200


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _config(outbound: dict, port: int) -> dict:
    return {
        "log": {"level": "error"},
        "inbounds": [
            {"type": "http", "tag": "http-in", "listen": "127.0.0.1", "listen_port": port}
        ],
        "outbounds": [outbound],
        "route": {"final": outbound.get("tag", "proxy")},
    }


def _request(port: int, url: str, expect: int, timeout: float) -> bool:
    proxy = f"http://127.0.0.1:{port}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )
    request = urllib.request.Request(url, headers={"User-Agent": "vpn-filtered-core-check"})
    try:
        with opener.open(request, timeout=timeout) as response:
            return response.getcode() == expect
    except urllib.error.HTTPError as exc:
        return exc.code == expect
    except Exception:  # noqa: BLE001
        return False


def verify(
    items: list,
    sing_box: str,
    work_dir: str,
    timeout: float = 12.0,
    log=print,
) -> list:
    """Возвращает только те конфиги, что реально открыли YouTube и Telegram."""
    if not items:
        return []

    os.makedirs(work_dir, exist_ok=True)
    survivors = []
    for index, item in enumerate(items, 1):
        uri = item.get("uri") if isinstance(item, dict) else str(item)
        outbound, reason = uris.parse_uri(uri, "proxy")
        if outbound is None:
            log(f"core-check: [{index}] пропуск — {reason}")
            continue

        port = _free_port()
        config_path = os.path.join(work_dir, f"core-{index}.json")
        with open(config_path, "w", encoding="utf-8") as handle:
            json.dump(_config(outbound, port), handle, ensure_ascii=False)
        log_path = os.path.join(work_dir, f"core-{index}.log")
        with open(log_path, "wb") as log_handle:
            process = subprocess.Popen(
                [sing_box, "run", "-c", config_path],
                stdout=log_handle,
                stderr=subprocess.STDOUT,
            )
        try:
            time.sleep(1.0)
            if process.poll() is not None:
                log(f"core-check: [{index}] ядро не запустилось")
                continue
            youtube_ok = _request(port, YOUTUBE_URL, YOUTUBE_CODE, timeout)
            telegram_ok = youtube_ok and _request(port, TELEGRAM_URL, TELEGRAM_CODE, timeout)
            if youtube_ok and telegram_ok:
                survivors.append(item)
                log(f"core-check: [{index}] ✅ YouTube и Telegram открылись")
            else:
                log(
                    f"core-check: [{index}] ❌ выброшен "
                    f"(YouTube={'ок' if youtube_ok else 'нет'}, "
                    f"Telegram={'ок' if telegram_ok else 'нет'})"
                )
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()

    return survivors


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: core_verify.py <list-file> <sing-box>")
        return 2
    path, sing_box = sys.argv[1], sys.argv[2]
    with open(path, encoding="utf-8") as handle:
        items = [{"uri": line.strip()} for line in handle if line.strip()]
    work = tempfile.mkdtemp(prefix="coreverify-")
    kept = verify(items, sing_box, work)
    print(f"итог: {len(kept)} из {len(items)} реально работают")
    for item in kept:
        print(" ", item["uri"][:80])
    return 0


if __name__ == "__main__":
    sys.exit(main())
