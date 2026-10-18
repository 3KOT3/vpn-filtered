"""Сквозная проверка серверного чекера: служба -> воркер (заглушка).

Запускает deploy/checker-service/server.py с поддельным репозиторием, где
check.py мгновенно пишет результат, и смотрит, что прогресс и публикация
действительно доходят до воркера.
"""

import http.server
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(os.path.dirname(HERE))
SERVICE = os.path.join(WORKSPACE, "deploy", "checker-service", "server.py")

RESULTS = {"progress": [], "publish": [], "started_at": None}


class MockWorker(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_POST(self):
        length = int(self.headers.get("content-length") or 0)
        body = self.rfile.read(length).decode("utf-8") if length else "{}"
        payload = json.loads(body or "{}")
        if self.path.startswith("/progress"):
            RESULTS["progress"].append(payload)
        elif self.path.startswith("/publish"):
            RESULTS["publish"].append(payload)
        else:
            self.send_response(404)
            self.end_headers()
            return
        data = b'{"ok":true}'
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        data = b'{"ok":true}'
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


FAKE_CHECKER = '''
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
parser = argparse.ArgumentParser()
parser.add_argument("--out-dir"); parser.add_argument("--work-dir")
parser.add_argument("--cache-dir"); parser.add_argument("--sing-box")
parser.add_argument("--min-mbps"); parser.add_argument("--source-files")
parser.add_argument("--progress-url", default=""); parser.add_argument("--progress-key", default="")
args = parser.parse_args()

def progress(percent, stage):
    if not args.progress_url:
        return
    import urllib.request, urllib.parse
    url = args.progress_url + (("?key=" + urllib.parse.quote(args.progress_key)) if args.progress_key else "")
    request = urllib.request.Request(url, data=json.dumps({
        "percent": percent, "stage": stage, "done": percent, "total": 100,
        "eta_sec": 0, "elapsed_sec": 1,
    }).encode(), method="POST")
    request.add_header("content-type", "application/json")
    urllib.request.urlopen(request, timeout=10).read()

os.makedirs(args.out_dir, exist_ok=True)
progress(20, "Проверка YouTube")
progress(60, "Проверка Telegram")
progress(90, "Замер скорости")
open(os.path.join(args.out_dir, "1.txt"), "w").write("vmess://test1\\nvmess://test2\\n")
open(os.path.join(args.out_dir, "auto.json"), "w").write('{"outbounds":[]}')
json.dump({"counts": {"kept": 2}}, open(os.path.join(args.out_dir, "status.json"), "w"))
progress(100, "Готово: в списке 2 конфигов")
'''


def wait_for(predicate, timeout=60, step=0.4):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            return True
        time.sleep(step)
    return False


def main() -> int:
    tmp = tempfile.mkdtemp(prefix="svc-test-")
    repo = os.path.join(tmp, "repo")
    os.makedirs(os.path.join(repo, "checker"), exist_ok=True)
    with open(os.path.join(repo, "checker", "check.py"), "w", encoding="utf-8") as fh:
        fh.write(FAKE_CHECKER)

    mock_port = 8098
    mock = http.server.ThreadingHTTPServer(("127.0.0.1", mock_port), MockWorker)
    threading.Thread(target=mock.serve_forever, daemon=True).start()

    env = dict(os.environ)
    env.update(
        {
            "CHECKER_KEY": "secret-key",
            "WORKER_URL": f"http://127.0.0.1:{mock_port}",
            "PORT": "8097",
            "INTERVAL_HOURS": "0",
            "REPO_ROOT": repo,
            "WORK_DIR": os.path.join(tmp, "work"),
            "SING_BOX": "",
        }
    )
    service = subprocess.Popen(
        [sys.executable, SERVICE],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    failures = []

    def check(condition, label):
        print(("  OK   " if condition else "  FAIL ") + label)
        if not condition:
            failures.append(label)

    try:
        check(wait_for(lambda: ping(8097, "/health")[0] == 200), "служба поднялась на порту 8097")

        code, body = post(8097, "/check?key=wrong")
        check(code == 403, "чужой ключ отклонён (403)")

        code, body = post(8097, "/check?key=secret-key")
        data = json.loads(body or "{}")
        check(code == 200 and data.get("started") is True, "запуск по правильному ключу принят")

        code, body = post(8097, "/check?key=secret-key")
        data = json.loads(body or "{}")
        check(code == 200 and data.get("started") is False, "повторный запуск не дублируется")

        finished = wait_for(
            lambda: json.loads(get(8097, "/state?key=secret-key")[1] or "{}").get("busy") is False
            and json.loads(get(8097, "/state?key=secret-key")[1] or "{}").get("finished_at"),
            timeout=90,
        )
        state = json.loads(get(8097, "/state?key=secret-key")[1] or "{}")
        check(finished, "прогон завершился")
        check(state.get("ok") is True, "итог помечен успешным")
        check(state.get("kept") == 2, f"в списке 2 конфига (получено {state.get('kept')})")

        check(len(RESULTS["progress"]) >= 4, f"прогресс дошёл до воркера ({len(RESULTS['progress'])} отчётов)")
        percents = [p.get("percent") for p in RESULTS["progress"]]
        check(percents == sorted(percents), f"проценты не уменьшаются: {percents}")
        check(percents and percents[-1] == 100, "последний отчёт — 100%")

        check(len(RESULTS["publish"]) == 1, f"список опубликован один раз ({len(RESULTS['publish'])})")
        if RESULTS["publish"]:
            payload = RESULTS["publish"][0]
            check("vmess://test1" in payload.get("plain", ""), "в публикации есть конфиги")
            check("auto" in payload and "status" in payload, "в публикации есть auto и status")
    finally:
        service.terminate()
        try:
            service.wait(timeout=10)
        except Exception:
            service.kill()
        mock.shutdown()

    print()
    if failures:
        print(f"ПРОВАЛОВ: {len(failures)}")
        return 1
    print("всё прошло")
    return 0


def ping(port, path):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=5) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc)


def get(port, path):
    return ping(port, path)


def post(port, path):
    request = urllib.request.Request(f"http://127.0.0.1:{port}{path}", data=b"{}", method="POST")
    request.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc)


if __name__ == "__main__":
    sys.exit(main())
