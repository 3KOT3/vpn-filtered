"""Проверка конфигов так, как это делает КЛИЕНТ (v2Box и любой другой).

Скрипт поднимает sing-box с HTTP-прокси на локальном порту и реально
запрашивает YouTube и Telegram через этот прокси — то есть ровно тем путём,
которым ходит браузер и клиент после подключения.

Запуск:
    python core_check.py <файл со списком> [--sing-box путь]
Результат: по каждому конфигу коды ответов YouTube и Telegram.
"""

from __future__ import annotations

import argparse
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
sys.path.insert(0, HERE)

import uris  # noqa: E402


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def build_config(outbound: dict, port: int) -> dict:
    tag = outbound.get("tag", "proxy")
    return {
        "log": {"level": "warn"},
        "inbounds": [
            {
                "type": "http",
                "tag": "http-in",
                "listen": "127.0.0.1",
                "listen_port": port,
            }
        ],
        "outbounds": [outbound],
        "route": {"final": tag},
    }


def probe(port: int, url: str, expect: int, timeout: float = 12.0):
    proxy = f"http://127.0.0.1:{port}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )
    request = urllib.request.Request(url, headers={"User-Agent": "vpn-filtered-core-check"})
    try:
        with opener.open(request, timeout=timeout) as response:
            code = response.getcode()
        return code == expect, code
    except urllib.error.HTTPError as exc:
        return exc.code == expect, exc.code
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("list_file")
    parser.add_argument("--sing-box", required=True)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    with open(args.list_file, encoding="utf-8") as handle:
        lines = [line.strip() for line in handle if line.strip()]
    if args.limit:
        lines = lines[: args.limit]

    print(f"конфигов к проверке: {len(lines)}")
    print(f"ядро: {args.sing_box}")
    print()

    work = tempfile.mkdtemp(prefix="corecheck-")
    good = 0
    for index, line in enumerate(lines, 1):
        outbound, reason = uris.parse_uri(line, "proxy")
        if outbound is None:
            print(f"[{index:>2}] пропуск: {reason}")
            continue
        port = free_port()
        config_path = os.path.join(work, f"c{index}.json")
        with open(config_path, "w", encoding="utf-8") as handle:
            json.dump(build_config(outbound, port), handle, ensure_ascii=False)

        log_path = os.path.join(work, f"c{index}.log")
        with open(log_path, "wb") as log_handle:
            process = subprocess.Popen(
                [args.sing_box, "run", "-c", config_path],
                stdout=log_handle,
                stderr=subprocess.STDOUT,
            )
        try:
            time.sleep(1.2)
            if process.poll() is not None:
                print(f"[{index:>2}] ядро не запустилось — {line[:60]}")
                continue
            yt_ok, yt_code = probe(port, "http://www.youtube.com/generate_204", 204)
            tg_ok, tg_code = probe(port, "https://core.telegram.org/", 200)
            mark = "✅" if (yt_ok and tg_ok) else "❌"
            if yt_ok and tg_ok:
                good += 1
            proto = outbound.get("type", "?")
            print(f"[{index:>2}] {mark} {proto:<6} YouTube={yt_code} Telegram={tg_code}  {line[:52]}")
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()

    print()
    print(f"итог: {good} из {len(lines)} открывают и YouTube, и Telegram через туннель")
    return 0


if __name__ == "__main__":
    sys.exit(main())
