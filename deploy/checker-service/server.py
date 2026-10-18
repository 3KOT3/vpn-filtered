#!/usr/bin/env python3
"""Серверная проверка VPN-конфигов для бота.

Зачем это нужно
---------------
Проверять «работает ли прокси из России» можно только из России: у Cloudflare
и GitHub серверы за границей, и они видят другую картину. Раньше проверку
запускал компьютер владельца — и стоило его выключить, как список переставал
обновляться.

Эта служба живёт на любом постоянном хосте (VPS в РФ, домашний мини-сервер,
Raspberry Pi) и делает всё сама:

  * раз в `INTERVAL_HOURS` часов запускает checker/check.py;
  * по кнопке «Обновить» в боте — запускает проверку немедленно;
  * прогресс отправляет прямо в бота (полоса загрузки живая, а не по шагам);
  * готовый список публикует в Cloudflare, откуда его берёт подписка.

Запуск
------
    CHECKER_KEY=... WORKER_URL=https://moybot.<аккаунт>.workers.dev python3 server.py

Эндпоинты
---------
    GET  /health        — жив ли, когда последний прогон
    POST /check?key=... — запустить проверку сейчас
    GET  /state?key=... — идёт ли прогон, что в последнем
"""

from __future__ import annotations

import http.server
import json
import os
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.environ.get("REPO_ROOT") or os.path.dirname(os.path.dirname(HERE))
CHECKER = os.path.join(REPO_ROOT, "checker", "check.py")
WORK_DIR = os.environ.get("WORK_DIR") or os.path.join(HERE, "work")

CHECKER_KEY = os.environ.get("CHECKER_KEY", "")
WORKER_URL = (os.environ.get("WORKER_URL") or "").rstrip("/")
PORT = int(os.environ.get("PORT") or 8099)
INTERVAL_HOURS = float(os.environ.get("INTERVAL_HOURS") or 6)
SING_BOX = os.environ.get("SING_BOX") or "sing-box"
SOURCES = os.environ.get("SOURCES") or ""
MIN_MBPS = os.environ.get("MIN_MBPS") or ""

_lock = threading.Lock()
_state = {
    "busy": False,
    "started_at": None,
    "finished_at": None,
    "ok": None,
    "kept": None,
    "error": None,
    "duration_sec": None,
}


def log(message: str = "") -> None:
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{stamp}] {message}", flush=True)


def post_json(url: str, payload: dict, timeout: int = 60) -> tuple:
    """POST JSON и вернуть (status, body). Ошибки не бросаем — вернём их текстом."""
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(url, data=data, method="POST")
    request.add_header("content-type", "application/json; charset=utf-8")
    request.add_header("user-agent", "vpn-checker-service")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        with open(os.devnull, "w") as null:
            del null
        try:
            body = exc.read().decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            body = ""
        return exc.code, body
    except Exception as exc:  # noqa: BLE001
        return 0, f"{type(exc).__name__}: {exc}"


def publish(out_dir: str) -> tuple:
    """Отправляет результат боту — тот кладёт его в KV и отдаёт подпискам."""
    if not WORKER_URL:
        return 0, "WORKER_URL не задан"
    files = {}
    for name, key in (("1.txt", "plain"), ("auto.json", "auto"), ("status.json", "status")):
        path = os.path.join(out_dir, name)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                files[key] = handle.read()
    if not files.get("plain"):
        return 0, "check.py не создал 1.txt"
    url = f"{WORKER_URL}/publish?key={urllib.parse.quote(CHECKER_KEY)}"
    return post_json(url, files, timeout=120)


def run_check(reason: str = "вручную") -> dict:
    """Запускает check.py. Возвращает итог; состояние пишется в _state."""
    started = time.time()
    out_dir = os.path.join(WORK_DIR, "out")
    os.makedirs(out_dir, exist_ok=True)
    cmd = [
        sys.executable,
        CHECKER,
        "--out-dir", out_dir,
        "--work-dir", os.path.join(WORK_DIR, "singbox"),
        "--cache-dir", os.path.join(WORK_DIR, "sources"),
    ]
    if SING_BOX:
        cmd += ["--sing-box", SING_BOX]
    if SOURCES:
        cmd += ["--source-files", SOURCES]
    if MIN_MBPS:
        cmd += ["--min-mbps", MIN_MBPS]
    if WORKER_URL:
        cmd += [
            "--progress-url",
            f"{WORKER_URL}/progress?key={urllib.parse.quote(CHECKER_KEY)}",
            "--progress-key", CHECKER_KEY,
        ]

    log(f"запуск проверки ({reason}): {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    duration = round(time.time() - started, 1)

    if result.returncode != 0:
        log(f"check.py завершился с кодом {result.returncode}")
        return {
            "ok": False,
            "error": f"код {result.returncode}",
            "duration_sec": duration,
            "kept": None,
        }

    status = 0
    body = ""
    for attempt in range(3):
        status, body = publish(out_dir)
        if status == 200:
            break
        log(f"публикация не удалась (HTTP {status}): {body[:120]}, попытка {attempt + 1}/3")
        time.sleep(5)

    kept = None
    status_path = os.path.join(out_dir, "status.json")
    if os.path.exists(status_path):
        try:
            with open(status_path, encoding="utf-8") as handle:
                kept = (json.load(handle).get("counts") or {}).get("kept")
        except Exception:  # noqa: BLE001
            kept = None

    ok = status == 200
    log(f"проверка закончена за {duration} с, в списке {kept}, публикация {'успешна' if ok else 'не удалась'}")
    return {
        "ok": ok,
        "error": None if ok else f"публикация HTTP {status}",
        "duration_sec": duration,
        "kept": kept,
    }


def start_check(reason: str) -> tuple:
    """Запускает проверку в фоне, если она ещё не идёт."""
    with _lock:
        if _state["busy"]:
            return False, "уже идёт"
        _state.update(
            {
                "busy": True,
                "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "error": None,
            }
        )

    def target():
        try:
            result = run_check(reason)
        except Exception as exc:  # noqa: BLE001
            result = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
        with _lock:
            _state.update(result)
            _state["busy"] = False
            _state["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    threading.Thread(target=target, daemon=True).start()
    return True, "запущено"


def scheduler() -> None:
    """Своя периодическая проверка: не зависим ни от cron, ни от чужого ПК."""
    if INTERVAL_HOURS <= 0:
        log("автозапуск выключен (INTERVAL_HOURS<=0)")
        return
    seconds = INTERVAL_HOURS * 3600
    log(f"автозапуск каждые {INTERVAL_HOURS:g} ч")
    time.sleep(20)  # даём сервису подняться
    while True:
        start_check("по расписанию")
        time.sleep(seconds)


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "vpn-checker/1.0"

    def log_message(self, fmt, *args):  # noqa: A003
        log("http: " + fmt % args)

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        with open(os.devnull, "wb") as null:
            del null
        self.wfile.write(body)

    def _authorized(self, query: dict) -> bool:
        if not CHECKER_KEY:
            return True
        return query.get("key", [""])[0] == CHECKER_KEY

    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        if parsed.path == "/health":
            self._send(200, {"ok": True, **_state, "interval_hours": INTERVAL_HOURS})
            return
        if parsed.path == "/state":
            if not self._authorized(query):
                self._send(403, {"ok": False, "error": "forbidden"})
                return
            self._send(200, {"ok": True, **_state})
            return
        self._send(404, {"ok": False, "error": "not found"})

    def do_POST(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        if parsed.path != "/check":
            self._send(404, {"ok": False, "error": "not found"})
            return
        if not self._authorized(query):
            self._send(403, {"ok": False, "error": "forbidden"})
            return
        started, message = start_check("кнопка в боте")
        self._send(200, {"ok": True, "started": started, "message": message, **_state})


def main() -> int:
    if not CHECKER_KEY:
        log("ВНИМАНИЕ: CHECKER_KEY не задан — сервис открыт всем. Задайте его.")
    if not os.path.exists(CHECKER):
        log(f"не найден чекер: {CHECKER}")
        return 1
    if WORKER_URL:
        log(f"результаты уходят в {WORKER_URL}")
    else:
        log("ВНИМАНИЕ: WORKER_URL не задан — публиковать результат некуда")
    threading.Thread(target=scheduler, daemon=True).start()
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    log(f"слушаю порт {PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log("остановлен")
    return 0


if __name__ == "__main__":
    sys.exit(main())
