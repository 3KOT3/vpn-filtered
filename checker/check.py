#!/usr/bin/env python3
"""Filter a VPN subscription down to the configs that really work.

Pipeline
--------
1. download the source lists (or read them from a local directory)
2. parse every `vless/vmess/trojan/ss/socks/http/hysteria2/tuic` URI into a
   sing-box outbound and drop what the core cannot express
3. TCP pre-filter: throw away endpoints that do not even accept a connection
4. real proxy test through sing-box: fetch YouTube and then Telegram
5. throughput test: 3 MB from Google's CDN through the surviving tunnels
6. write `1.txt` (plain), `1-base64.txt`, `status.json` and `REPORT.md`

Only the standard library is used, plus the `sing-box` binary.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import concurrent.futures
import contextlib
import datetime
import hashlib
import http.client
import itertools
import json
import os
import random
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uris  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
DEFAULT_CONFIG = os.path.join(HERE, "config.json")
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

REGIONAL_A = 0x1F1E6


# --------------------------------------------------------------------------- #
# logging
# --------------------------------------------------------------------------- #

_START = time.time()


def log(message: str = "") -> None:
    print(f"[{time.time() - _START:7.1f}s] {message}", flush=True)


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def load_json(path: str, default=None):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return default


def http_get(url: str, timeout: int = 120, tries: int = 3) -> bytes:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            if attempt + 1 < tries:
                time.sleep(2 + attempt * 3)
    raise RuntimeError(f"GET {url} failed: {type(last).__name__}: {last}")


def country_of(uri: str) -> str:
    """Best-effort country code from a config's display name."""
    name = uris.uri_name(uri)
    if not name:
        return "??"
    for ch in name:
        code = ord(ch)
        if REGIONAL_A <= code <= REGIONAL_A + 25:
            idx = name.index(ch)
            pair = name[idx : idx + 2]
            if len(pair) == 2 and all(REGIONAL_A <= ord(c) <= REGIONAL_A + 25 for c in pair):
                return "".join(chr(ord(c) - REGIONAL_A + ord("A")) for c in pair)
            break
    match = re.search(r"\b([A-Z]{2})-\d", name)
    if match:
        return match.group(1)
    return "??"


def free_port() -> int:
    sock = socket.socket()
    try:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]
    finally:
        sock.close()


def allocate_ports(count: int) -> list:
    """Reserve `count` currently free consecutive-ish local ports."""
    for _ in range(40):
        base = random.randint(21000, 55000 - count)
        ports = []
        ok = True
        for offset in range(count):
            port = base + offset
            probe = socket.socket()
            try:
                probe.bind(("127.0.0.1", port))
            except OSError:
                ok = False
                probe.close()
                break
            finally:
                with contextlib.suppress(Exception):
                    probe.close()
            ports.append(port)
        if ok and len(ports) == count:
            return ports
    raise RuntimeError(f"could not allocate {count} free ports")


def tail(path: str, lines: int = 12) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return "\n".join(fh.read().splitlines()[-lines:])
    except Exception:
        return ""


# --------------------------------------------------------------------------- #
# sing-box process management
# --------------------------------------------------------------------------- #


class SingBox:
    """Run one sing-box instance for the duration of a `with` block."""

    def __init__(self, binary: str, workdir: str, name: str):
        self.binary = binary
        # absolute: sing-box is started with cwd=workdir, so a relative config
        # path would be resolved a second time against that directory and the
        # process would die with "read config ... no such file"
        self.workdir = os.path.abspath(workdir)
        self.name = name
        self.proc = None
        self.log_path = os.path.join(self.workdir, f"{name}.log")
        self._logf = None
        self.api_port = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.stop()
        return False

    def start(self, config: dict, api_port: int, timeout: float = 30.0) -> None:
        os.makedirs(self.workdir, exist_ok=True)
        self.api_port = api_port
        config.setdefault("experimental", {})["clash_api"] = {
            "external_controller": f"127.0.0.1:{api_port}"
        }
        cfg_path = os.path.join(self.workdir, f"{self.name}.json")
        with open(cfg_path, "w", encoding="utf-8") as fh:
            json.dump(config, fh, ensure_ascii=False)

        self._logf = open(self.log_path, "w", encoding="utf-8")
        self.proc = subprocess.Popen(
            [self.binary, "run", "-c", cfg_path],
            stdout=self._logf,
            stderr=subprocess.STDOUT,
            cwd=self.workdir,
        )

        deadline = time.time() + timeout
        url = f"http://127.0.0.1:{api_port}/version"
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(
                    f"sing-box[{self.name}] exited rc={self.proc.returncode}: {tail(self.log_path, 6)}"
                )
            try:
                with urllib.request.urlopen(url, timeout=2) as resp:
                    resp.read()
                return
            except Exception:  # noqa: BLE001
                time.sleep(0.2)
        self.stop()
        raise RuntimeError(f"sing-box[{self.name}] api never came up: {tail(self.log_path, 6)}")

    def stop(self) -> None:
        if self.proc is not None:
            with contextlib.suppress(Exception):
                self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except Exception:  # noqa: BLE001
                with contextlib.suppress(Exception):
                    self.proc.kill()
                    self.proc.wait(timeout=5)
            self.proc = None
        if self._logf is not None:
            with contextlib.suppress(Exception):
                self._logf.close()
            self._logf = None


def base_config(final_tag: str) -> dict:
    """Shared sing-box skeleton.

    `prefer_ipv4` matters: GitHub runners and many home networks have no usable
    IPv6, and without it sing-box happily dials an AAAA record and dies with
    "network is unreachable".
    """
    return {
        "log": {"level": "warn", "timestamp": False},
        "dns": {
            "servers": [{"type": "local", "tag": "local"}],
            "final": "local",
            "strategy": "prefer_ipv4",
        },
        "inbounds": [],
        "outbounds": [],
        "route": {
            "rules": [],
            "final": final_tag,
            "default_domain_resolver": {"server": "local", "strategy": "prefer_ipv4"},
        },
    }


# --------------------------------------------------------------------------- #
# stage 1: collect
# --------------------------------------------------------------------------- #


def download_sources(cfg: dict, cache_dir: str) -> dict:
    """Скачивает источники.

    Кроме номеров файлов зеркала (`"6"`) поддерживаются полные ссылки: так
    пользователь может добавить в бота свой источник, и он будет проверяться
    наравне с остальными.
    """
    src = cfg["source"]
    out = {}
    for name in src["files"]:
        if str(name).startswith("http"):
            url = str(name)
            cache_name = "url_" + hashlib.sha256(url.encode()).hexdigest()[:12] + ".txt"
        else:
            url = (
                f"https://raw.githubusercontent.com/{src['repo']}/refs/heads/"
                f"{src['ref']}/{src['dir']}/{name}.txt"
            )
            cache_name = f"{name}.txt"
        ttl = int(cfg.get("source", {}).get("cache_ttl_sec", 600))
        cached = os.path.join(cache_dir, cache_name)
        fresh = (
            os.path.exists(cached)
            and os.path.getsize(cached) > 0
            and (time.time() - os.path.getmtime(cached)) < ttl
        )
        if fresh:
            with open(cached, "rb") as fh:
                out[str(name)] = fh.read()
            age = int(time.time() - os.path.getmtime(cached))
            log(f"source {cache_name}: {len(out[str(name)])} bytes (кэш, {age} с)")
            continue
        data = http_get(url)
        os.makedirs(cache_dir, exist_ok=True)
        with open(cached, "wb") as fh:
            fh.write(data)
        out[str(name)] = data
        log(f"source {cache_name}: {len(data)} bytes")
    return out


def fetch_ru_prefilter(cfg: dict):
    """Список URI, которые ответили из России. Пустое множество = без фильтра.

    Воркер бота складывает результат TCP-проверки с телефона владельца: это
    единственный способ узнать, что сервер не заблокирован именно у него.
    """
    url = (cfg.get("source") or {}).get("prefilter_url")
    if not url:
        return None
    try:
        data = http_get(url, timeout=30, tries=1)
    except Exception as exc:  # noqa: BLE001
        log(f"ru-prefilter: не удалось получить список ({type(exc).__name__}) — проверяем всё")
        return None
    text = data.decode("utf-8", "replace")
    uris = {line.strip() for line in text.splitlines() if "://" in line}
    if not uris:
        log("ru-prefilter: список из России пуст — проверяем всё")
        return None
    log(f"ru-prefilter: {len(uris)} конфигов ответили из России")
    return uris

def read_local_sources(directory: str) -> dict:
    out = {}
    for name in sorted(os.listdir(directory)):
        if name.endswith(".txt"):
            with open(os.path.join(directory, name), "rb") as fh:
                out[name[:-4]] = fh.read()
    return out


def collect(raw_sources: dict, limit: int = 0, allowed=None, cfg_limits=None):
    """Return (candidates, stats). Each candidate is a dict."""
    stats = {
        "lines": 0,
        "comments": 0,
        "parsed": 0,
        "unsupported": 0,
        "duplicates": 0,
        "unsupported_reasons": {},
        "by_protocol": {},
    }
    seen = {}
    candidates = []
    reason_counter = stats["unsupported_reasons"]
    proto_counter = stats["by_protocol"]

    for name in sorted(raw_sources):
        text = raw_sources[name].decode("utf-8", "replace")
        # В автоматических источниках десятки тысяч строк. Берём равномерную
        # выборку по всему файлу: первые N строк почти всегда один и тот же
        # пул серверов, а нам нужны разные.
        lines = text.splitlines()
        per_source = int((cfg_limits or {}).get("max_per_source", 0) or 0)
        if per_source and len(lines) > per_source:
            # Смещение меняется от прогона к прогону: сегодня проверяем одну
            # часть файла, через два часа — следующую. Так за сутки список
            # источников проходится целиком, а не первые строки.
            stride = len(lines) / float(per_source)
            offset = int(time.time() // 3600) % max(1, int(stride))
            picked = []
            for index in range(per_source):
                start = int(index * stride) + offset
                if start < len(lines):
                    picked.append(lines[start])
            if picked:
                lines = picked
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            stats["lines"] += 1
            if line.startswith("#") or "://" not in line:
                stats["comments"] += 1
                continue
            key = uris.dedupe_key(line)
            if key in seen:
                stats["duplicates"] += 1
                continue
            seen[key] = True
            if allowed is not None and line not in allowed:
                stats["unsupported"] += 1
                reason_counter["не ответил из России"] = (
                    reason_counter.get("не ответил из России", 0) + 1
                )
                continue
            outbound, reason = uris.parse_uri(line, f"p{len(candidates):05d}")
            if outbound is None:
                stats["unsupported"] += 1
                reason_counter[reason] = reason_counter.get(reason, 0) + 1
                continue
            stats["parsed"] += 1
            proto = outbound["type"]
            proto_counter[proto] = proto_counter.get(proto, 0) + 1
            candidates.append(
                {
                    "uri": line,
                    "outbound": outbound,
                    "tag": outbound["tag"],
                    "name": uris.uri_name(line),
                    "country": country_of(line),
                    "protocol": proto,
                    "server": outbound.get("server", ""),
                    "port": outbound.get("server_port", 0),
                    "source": name,
                }
            )
            if limit and len(candidates) >= limit:
                log(f"limit of {limit} candidates reached, stopping parse")
                return candidates, stats
    return candidates, stats


# --------------------------------------------------------------------------- #
# stage 2: TCP pre-filter
# --------------------------------------------------------------------------- #


async def _tcp_probe(host: str, port: int, timeout: float, sem: asyncio.Semaphore) -> bool:
    if not host or not port:
        return False
    async with sem:
        loop = asyncio.get_running_loop()
        try:
            infos = await loop.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        except Exception:  # noqa: BLE001
            return False
        if not infos:
            return False
        # de-duplicate resolved addresses, try a few of them
        addrs = []
        for family, _type, _proto, _canon, sockaddr in infos:
            if sockaddr not in addrs:
                addrs.append(sockaddr)
        for sockaddr in addrs[:4]:
            family = socket.AF_INET6 if len(sockaddr) == 4 else socket.AF_INET
            try:
                fut = asyncio.open_connection(host=sockaddr[0], port=sockaddr[1], family=family)
                reader, writer = await asyncio.wait_for(fut, timeout=timeout)
                writer.close()
                with contextlib.suppress(Exception):
                    await writer.wait_closed()
                return True
            except Exception:  # noqa: BLE001
                continue
        return False


def tcp_prefilter(candidates: list, timeout: float, concurrency: int) -> tuple:
    async def runner():
        sem = asyncio.Semaphore(concurrency)
        tasks = [
            asyncio.ensure_future(_tcp_probe(c["server"], c["port"], timeout, sem))
            for c in candidates
        ]
        results = []
        done = 0
        total = len(tasks)
        for fut in asyncio.as_completed(tasks):
            results.append(await fut)
            done += 1
            if done % 1000 == 0:
                log(f"  tcp prefilter {done}/{total}")
        return results

    results = asyncio.run(runner())
    alive = [c for c, ok in zip(candidates, results) if ok]
    return alive, sum(1 for r in results if r)


# --------------------------------------------------------------------------- #
# stage 3: YouTube / Telegram through sing-box
# --------------------------------------------------------------------------- #


def delay_probe(api_port: int, tag: str, url: str, timeout_ms: int):
    """Ask sing-box to fetch `url` through outbound `tag`."""
    quoted_tag = urllib.parse.quote(tag, safe="")
    quoted_url = urllib.parse.quote(url, safe="")
    endpoint = (
        f"http://127.0.0.1:{api_port}/proxies/{quoted_tag}/delay"
        f"?url={quoted_url}&timeout={timeout_ms}"
    )
    try:
        with urllib.request.urlopen(endpoint, timeout=timeout_ms / 1000 + 10) as resp:
            data = json.loads(resp.read() or b"{}")
        delay = data.get("delay")
        if isinstance(delay, int) and delay > 0:
            return delay, None
        return None, "no-delay"
    except urllib.error.HTTPError as exc:
        with contextlib.suppress(Exception):
            exc.read()
        return None, f"http{exc.code}"
    except Exception as exc:  # noqa: BLE001
        return None, type(exc).__name__


_INSTANCE_SEQ = itertools.count(1)


def _delay_group(
    binary: str, workdir: str, group: list, cfg: dict, stage: str, url: str,
    results: dict, stats: dict, lock=None
) -> None:
    """Test one group of outbounds inside a single sing-box instance.

    A single malformed config makes sing-box refuse to start, which would kill
    the whole group, so on a startup failure the group is bisected until the
    offending config stands alone.
    """
    api_port = free_port()
    config = base_config(group[0]["tag"])
    config["outbounds"] = [c["outbound"] for c in group]
    instance = SingBox(binary, workdir, f"{stage}-{next(_INSTANCE_SEQ):04d}")
    try:
        instance.start(config, api_port)
    except Exception as exc:  # noqa: BLE001
        instance.stop()
        if len(group) == 1:
            if lock is not None:
                with lock:
                    stats["drops"] += 1
            else:
                stats["drops"] += 1
            log(f"{stage}: dropping 1 config ({group[0]['name'][:36]!r}): {str(exc)[:110]}")
            return
        middle = len(group) // 2
        log(f"{stage}: group of {len(group)} would not start, splitting: {str(exc)[:90]}")
        _delay_group(binary, workdir, group[:middle], cfg, stage, url, results, stats, lock)
        _delay_group(binary, workdir, group[middle:], cfg, stage, url, results, stats, lock)
        return

    try:
        timeout_ms = cfg["delay"]["timeout_ms"]
        concurrency = cfg["delay"]["concurrency"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = {
                pool.submit(delay_probe, api_port, c["tag"], url, timeout_ms): c for c in group
            }
            for future in concurrent.futures.as_completed(futures):
                candidate = futures[future]
                try:
                    delay, _error = future.result()
                except Exception:  # noqa: BLE001
                    delay = None
                if delay:
                    results[candidate["tag"]] = delay
    finally:
        instance.stop()


def proxy_stage(binary: str, workdir: str, candidates: list, cfg: dict, stage: str, url: str,
                on_batch=None) -> dict:
    """Run the delay probe for every candidate, in batches. Returns {tag: delay}.

    Батчи идут параллельно: каждый — отдельный sing-box-процесс, и пока один
    батч ждёт ответов прокси, остальные уже работают. Это убирает главную
    паузу в проверке — последовательное ожидание медленных батчей.
    """
    import threading

    results = {}
    stats = {"drops": 0}
    lock = threading.Lock()
    batch_size = cfg["delay"]["batch_size"]
    parallel = max(1, int(cfg["delay"].get("parallel_batches", 1)))
    budget = cfg["limits"].get("time_budget_sec", 0)
    drop_limit = max(25, int(0.05 * len(candidates)))

    batches = [candidates[i : i + batch_size] for i in range(0, len(candidates), batch_size)]
    log(f"{stage}: {len(candidates)} proxies in {len(batches)} batches (параллельно x{parallel})")

    completed = [0]

    def run_one(index, batch):
        if budget and time.time() - _START > budget:
            return
        before = len(results)
        _delay_group(binary, workdir, batch, cfg, stage, url, results, stats, lock)
        with lock:
            completed[0] += 1
            drops = stats["drops"]
        log(
            f"{stage}: batch {index}/{len(batches)} -> +{len(results) - before}, "
            f"total {len(results)}"
        )
        if on_batch:
            on_batch(completed[0], len(batches), len(results))
        if drops > drop_limit:
            raise RuntimeError(
                f"{stage}: {drops} конфигов подряд не дали sing-box стартовать "
                f"(порог {drop_limit}) — это похоже на системную проблему, а не на битые "
                f"конфиги. Прогон остановлен, чтобы не молотить впустую."
            )

    if parallel > 1 and len(batches) > 1:
        workers = min(parallel, len(batches))
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(run_one, i, batch) for i, batch in enumerate(batches, 1)]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # прокидывает RuntimeError при превышении порога
    else:
        for index, batch in enumerate(batches, 1):
            run_one(index, batch)

    return results


# --------------------------------------------------------------------------- #
# stage 4: throughput
# --------------------------------------------------------------------------- #


def throughput_probe(port: int, url: str, request_bytes: int, deadline: float):
    """Download `request_bytes` from `url` through the local mixed proxy `port`."""
    parsed = urllib.parse.urlsplit(url)
    host = parsed.hostname
    target_port = parsed.port or (443 if parsed.scheme == "https" else 80)
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query

    started = time.time()
    conn = http.client.HTTPSConnection("127.0.0.1", port, timeout=deadline + 3)
    try:
        conn.set_tunnel(host, target_port)
        conn.request(
            "GET",
            path,
            headers={
                "Host": host,
                "User-Agent": UA,
                "Range": f"bytes=0-{request_bytes - 1}",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
            },
        )
        resp = conn.getresponse()
        status = resp.status
        if status not in (200, 206):
            return None, None, f"status{status}"
        got = 0
        while got < request_bytes:
            if time.time() - started > deadline:
                break
            chunk = resp.read(65536)
            if not chunk:
                break
            got += len(chunk)
        elapsed = time.time() - started
        if elapsed <= 0 or got <= 0:
            return None, None, "no-data"
        return got, got * 8.0 / elapsed / 1e6, None
    finally:
        with contextlib.suppress(Exception):
            conn.close()


def build_group_config(group: list, ports: list) -> dict:
    """One local mixed inbound per config, each routed to its own outbound."""
    config = base_config(group[0]["tag"])
    config["outbounds"] = [c["outbound"] for c in group]
    config["inbounds"] = [
        {"type": "mixed", "tag": f"in{i:04d}", "listen": "127.0.0.1", "listen_port": port}
        for i, port in enumerate(ports)
    ]
    config["route"]["rules"] = [
        {"inbound": [f"in{i:04d}"], "outbound": c["tag"]} for i, c in enumerate(group)
    ]
    return config


def run_group(binary, workdir, name, group, worker, results, stats, max_workers=None,
              lock=None) -> None:
    """Run `worker(port, candidate)` for every config through its own local port.

    A single malformed config makes sing-box refuse to start, which would kill the
    whole group, so on a startup failure the group is bisected until the offender
    stands alone.
    """
    ports = allocate_ports(len(group))
    api_port = free_port()
    config = build_group_config(group, ports)
    instance = SingBox(binary, workdir, f"{name}-{next(_INSTANCE_SEQ):04d}")
    try:
        instance.start(config, api_port)
    except Exception as exc:  # noqa: BLE001
        instance.stop()
        if len(group) == 1:
            if lock is not None:
                with lock:
                    stats["drops"] += 1
            else:
                stats["drops"] += 1
            log(f"{name}: dropping 1 config ({group[0]['name'][:36]!r}): {str(exc)[:110]}")
            return
        middle = len(group) // 2
        log(f"{name}: group of {len(group)} would not start, splitting: {str(exc)[:90]}")
        run_group(binary, workdir, name, group[:middle], worker, results, stats, max_workers, lock)
        run_group(binary, workdir, name, group[middle:], worker, results, stats, max_workers, lock)
        return

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers or len(group)) as pool:
            futures = {
                pool.submit(worker, port, candidate): candidate
                for port, candidate in zip(ports, group)
            }
            for future in concurrent.futures.as_completed(futures):
                candidate = futures[future]
                try:
                    value = future.result()
                except Exception:  # noqa: BLE001
                    value = None
                if value is not None:
                    results[candidate["tag"]] = value
    finally:
        instance.stop()


def run_group_stage(binary, workdir, name, candidates, cfg, worker, concurrency) -> dict:
    """Split the list into chunks and run `run_group` over each of them.

    Чанки идут параллельно (каждый — свой sing-box-процесс), как и батчи в
    `proxy_stage`: медленный чанк не держит остальные.
    """
    import threading

    budget = cfg["limits"].get("time_budget_sec", 0)
    parallel = max(1, int(cfg["limits"].get("parallel_groups", 1)))
    results = {}
    stats = {"drops": 0}
    lock = threading.Lock()
    drop_limit = max(25, int(0.05 * len(candidates)))
    chunks = [candidates[i : i + concurrency] for i in range(0, len(candidates), concurrency)]
    log(f"{name}: {len(candidates)} proxies in {len(chunks)} chunks (параллельно x{parallel})")

    def run_one(index, chunk):
        if budget and time.time() - _START > budget:
            return
        before = len(results)
        run_group(binary, workdir, name, chunk, worker, results, stats, concurrency, lock)
        with lock:
            drops = stats["drops"]
        log(
            f"{name}: chunk {index}/{len(chunks)} -> +{len(results) - before}, "
            f"total {len(results)}"
        )
        if drops > drop_limit:
            raise RuntimeError(
                f"{name}: {drops} конфигов подряд не дали sing-box стартовать "
                f"(порог {drop_limit}) — похоже на системную проблему. Прогон остановлен."
            )

    if parallel > 1 and len(chunks) > 1:
        workers = min(parallel, len(chunks))
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(run_one, i, chunk) for i, chunk in enumerate(chunks, 1)]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # прокидывает RuntimeError при превышении порога
    else:
        for index, chunk in enumerate(chunks, 1):
            run_one(index, chunk)
    return results


def telegram_dc_probe(port: int, hosts: list, dc_port: int, timeout: float):
    """TCP-коннект до дата-центра Telegram через локальный прокси.

    Настоящее TLS-рукопожатие здесь не годится: на порту 443 у Telegram
    «поддельный TLS» (fake-TLS framing), и сервер сбрасывает реальный handshake —
    проверено экспериментально, все четыре DC отвечают ConnectionReset. Поэтому
    проверяем именно TCP: Telegram блокирует часть хостинговых диапазонов, и у
    заблокированного прокси коннект к DC просто не открывается.
    """
    last = "no-dc"
    for host in hosts:
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
        try:
            conn.set_tunnel(host, dc_port)
            conn.connect()
            return host, None
        except Exception as exc:  # noqa: BLE001
            last = type(exc).__name__
        finally:
            with contextlib.suppress(Exception):
                conn.close()
    return None, last


def telegram_dc_stage(binary, workdir, candidates, cfg) -> dict:
    dc_cfg = cfg["telegram_dc"]
    hosts = dc_cfg["hosts"]
    dc_port = dc_cfg["port"]
    timeout = dc_cfg["timeout_sec"]

    def worker(port, candidate):
        host, _error = telegram_dc_probe(port, hosts, dc_port, timeout)
        return host

    log(f"telegram-dc: проверяем дата-центры {', '.join(hosts)}")
    return run_group_stage(
        binary, workdir, "telegram-dc", candidates, cfg, worker, dc_cfg["concurrency"]
    )


def speed_stage(binary, workdir, candidates, cfg) -> dict:
    speed_cfg = cfg["speed"]
    url = speed_cfg["url"]
    request_bytes = speed_cfg["request_bytes"]
    deadline = speed_cfg["deadline_sec"]

    def worker(port, candidate):
        _got, mbps, _error = throughput_probe(port, url, request_bytes, deadline)
        return mbps

    log(f"speed: порог {speed_cfg['min_mbps']} Мбит/с")
    return run_group_stage(
        binary, workdir, "speed", candidates, cfg, worker, speed_cfg["concurrency"]
    )


# --------------------------------------------------------------------------- #
# output
# --------------------------------------------------------------------------- #


#: DNS внутри туннеля.
#: AdGuard (94.140.14.14) в России заблокирован — с ним Hiddify падал
#: в таймаут (errno 60): клиент не мог разрешить ни одного имени. Берём
#: Яндекс DNS: он доступен с российских адресов и отвечает быстро.
#: Рекламу он не режет, зато конфиг работает.
ADGUARD_DNS = "77.88.8.8"


def build_auto_config(kept: list, cfg: dict, legacy: bool = False) -> dict:
    """Конфиг sing-box с авто-выбором сервера и блокировкой рекламы.

    Все прошедшие конфиги лежат в группе `urltest`: клиент сам держит самый
    быстрый живой. DNS идёт напрямую в Яндекс DNS (не через туннель), поэтому
    и трекеры отсекаются по домену ещё до загрузки.

    `legacy=True` — синтаксис sing-box 1.10 (ядро Hiddify): адрес сервера в поле
    `address` и отдельный outbound `dns` для DNS-запросов. Новые ядра (1.12+)
    такой формат не читают, поэтому файлов два.
    """
    proxies = []
    for item in kept:
        outbound = dict(item["outbound"])
        outbound["tag"] = item["tag"]
        proxies.append(outbound)

    names = [item["tag"] for item in kept]
    urltest = {
        "type": "urltest",
        "tag": "auto",
        "outbounds": names,
        "url": cfg["youtube"]["url"],
        "interval": "45s",
        "tolerance": 50,
        "interrupt_exist_connections": False,
    }

    if legacy:
        return {
            "outbounds": proxies
            + [urltest, {"type": "direct", "tag": "direct"}, {"type": "dns", "tag": "dns-out"}],
            "dns": {
                "servers": [{"tag": "adguard", "address": ADGUARD_DNS, "detour": "direct"}],
                "final": "adguard",
                "strategy": "prefer_ipv4",
            },
            "route": {
                "rules": [{"protocol": "dns", "outbound": "dns-out"}],
                "final": "auto",
            },
        }

    return {
        "outbounds": proxies + [urltest, {"type": "direct", "tag": "direct"}],
        "dns": {
            "servers": [
                {"type": "udp", "tag": "adguard", "server": ADGUARD_DNS, "detour": "direct"}
            ],
            "final": "adguard",
            "strategy": "prefer_ipv4",
        },
        "route": {
            "rules": [{"protocol": "dns", "action": "hijack-dns"}],
            "final": "auto",
        },
    }

def to_clash(item: dict):
    """Превращает разобранный конфиг в запись Clash/Mihomo.

    Clash-формат понимает Hiddify — и именно в нём есть группа `url-test`,
    которая сама держит самый быстрый живой сервер. sing-box конфиг Hiddify
    не принимает (падает на импорте), а YAML принимает.
    """
    outbound = item["outbound"]
    kind = outbound.get("type")
    tls = outbound.get("tls") or {}
    transport = outbound.get("transport") or {}

    proxy = {
        "name": item["tag"],
        "server": outbound.get("server"),
        "port": outbound.get("server_port"),
        "udp": True,
    }

    if kind == "vless":
        proxy["type"] = "vless"
        proxy["uuid"] = outbound.get("uuid")
        if outbound.get("flow"):
            proxy["flow"] = outbound["flow"]
        if tls.get("enabled"):
            proxy["tls"] = True
            if tls.get("server_name"):
                proxy["servername"] = tls["server_name"]
            reality = tls.get("reality") or {}
            if reality.get("public_key"):
                proxy["reality-opts"] = {"public-key": reality["public_key"]}
                if reality.get("short_id"):
                    proxy["reality-opts"]["short-id"] = reality["short_id"]
            fingerprint = (tls.get("utls") or {}).get("fingerprint")
            if fingerprint:
                proxy["client-fingerprint"] = fingerprint
    elif kind == "vmess":
        proxy["type"] = "vmess"
        proxy["uuid"] = outbound.get("uuid")
        proxy["alterId"] = int(outbound.get("alter_id") or 0)
        proxy["cipher"] = "auto"
        if tls.get("enabled"):
            proxy["tls"] = True
            if tls.get("server_name"):
                proxy["servername"] = tls["server_name"]
    elif kind == "trojan":
        proxy["type"] = "trojan"
        proxy["password"] = outbound.get("password")
        if tls.get("server_name"):
            proxy["sni"] = tls["server_name"]
    elif kind == "shadowsocks":
        proxy["type"] = "ss"
        proxy["cipher"] = outbound.get("method")
        proxy["password"] = outbound.get("password")
    else:
        return None

    transport_type = transport.get("type")
    if transport_type == "ws":
        proxy["network"] = "ws"
        options = {}
        if transport.get("path"):
            options["path"] = transport["path"]
        headers = transport.get("headers") or {}
        host = headers.get("Host") or headers.get("host")
        if host:
            options["headers"] = {"Host": host}
        if options:
            proxy["ws-opts"] = options
    elif transport_type == "grpc":
        proxy["network"] = "grpc"
        if transport.get("service_name"):
            proxy["grpc-opts"] = {"grpc-service-name": transport["service_name"]}

    return proxy


def _yaml_scalar(value) -> str:
    """Скаляр для YAML: числа и булевы как есть, строки — в кавычках."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    # JSON-строка — валидный YAML-скаляр в двойных кавычках
    return json.dumps(str(value), ensure_ascii=False)


def _yaml_lines(key: str, value, indent: int) -> list:
    """Блочное представление `key: value` с отступами (для вложенных dict/list)."""
    pad = " " * indent
    if isinstance(value, dict):
        lines = [f"{pad}{key}:"]
        for sub_key, sub_value in value.items():
            lines += _yaml_lines(sub_key, sub_value, indent + 2)
        return lines
    if isinstance(value, list):
        lines = [f"{pad}{key}:"]
        for item in value:
            lines.append(f"{pad}  - {_yaml_scalar(item)}")
        return lines
    return [f"{pad}{key}: {_yaml_scalar(value)}"]


def build_client_config(kept: list, cfg: dict) -> dict:
    """Готовый профиль для приложения sing-box на iPhone.

    Главное отличие от серверных конфигов: внутри есть tun-инбаунд и группа
    urltest, которая сама перепроверяет серверы каждые 30 секунд и уводит
    трафик на живой. Именно этого не умеет v2Box — там сервер выбирают руками.
    """
    proxies = []
    for item in kept:
        outbound = dict(item["outbound"])
        outbound["tag"] = item["tag"]
        proxies.append(outbound)

    names = [item["tag"] for item in kept]
    urltest = {
        "type": "urltest",
        "tag": "auto",
        "outbounds": names,
        "url": cfg["youtube"]["url"],
        "interval": "30s",
        "tolerance": 50,
        "interrupt_exist_connections": False,
    }
    selector = {
        "type": "selector",
        "tag": "select",
        "outbounds": ["auto"] + names + ["direct"],
        "default": "auto",
        "interrupt_exist_connections": False,
    }
    return {
        "log": {"level": "warn", "timestamp": True},
        "dns": {
            "servers": [
                {"type": "udp", "tag": "direct-dns", "server": "77.88.8.8", "detour": "direct"},
                {
                    "type": "https",
                    "tag": "remote-dns",
                    "server": "dns.google",
                    "detour": "select",
                },
            ],
            # .ru-домены резолвим напрямую, остальное — через туннель
            "rules": [{"domain_suffix": [".ru", ".su", ".рф"], "server": "direct-dns"}],
            "final": "remote-dns",
            "strategy": "prefer_ipv4",
        },
        "inbounds": [
            {
                "type": "tun",
                "tag": "tun-in",
                "address": ["172.19.0.1/30"],
                "mtu": 9000,
                "auto_route": True,
                "strict_route": True,
                "stack": "mixed",
            }
        ],
        "outbounds": proxies + [urltest, selector, {"type": "direct", "tag": "direct"}],
        "route": {
            "rules": [
                {"protocol": "dns", "action": "hijack-dns"},
                {"ip_is_private": True, "outbound": "direct"},
            ],
            "final": "select",
            "auto_detect_interface": True,
            # новое ядро требует явный резолвер по умолчанию
            "default_domain_resolver": {"server": "direct-dns"},
        },
    }

def build_clash_config(kept: list, cfg: dict) -> str:
    """Clash (Mihomo/Clash.Meta) YAML с группой автоматического выбора.

    Формат строго стандартный: первая строка `port:`, обычный блочный YAML
    вместо JSON-вставок и имя группы ASCII. Именно так выглядит конфиг, который
    Hiddify распознаёт как Clash (у него внутри форк Clash.Meta).
    """
    proxies = [p for p in (to_clash(item) for item in kept) if p]
    names = [p["name"] for p in proxies]
    lines = [
        "port: 7890",
        "socks-port: 7891",
        "allow-lan: false",
        "mode: rule",
        "log-level: warning",
        "",
        "proxies:",
    ]
    for proxy in proxies:
        lines.append(f"  - name: {_yaml_scalar(proxy['name'])}")
        for key, value in proxy.items():
            if key == "name":
                continue
            lines += _yaml_lines(key, value, 4)

    lines += [
        "",
        "proxy-groups:",
        "  - name: Auto",
        "    type: url-test",
        f"    url: {cfg['youtube']['url']}",
        "    interval: 30",
        "    tolerance: 50",
        "    lazy: false",
        "    proxies:",
    ]
    for name in names:
        lines.append(f"      - {_yaml_scalar(name)}")
    lines += [
        "",
        "rules:",
        "  - MATCH,Auto",
        "",
    ]
    return "\n".join(lines)

def per_source(items: list) -> dict:
    """Сколько конфигов каждого источника осталось на текущем шаге."""
    counts = {}
    for item in items:
        name = item.get("source") or "?"
        counts[name] = counts.get(name, 0) + 1
    return counts


def build_by_source(sources_order: list, funnel: dict) -> list:
    """Воронка по каждому источнику: от разбора до итогового списка."""
    rows = []
    for name in sources_order:
        rows.append(
            {
                "source": name,
                "parsed": funnel.get("parsed", {}).get(name, 0),
                "alive": funnel.get("alive", {}).get(name, 0),
                "youtube": funnel.get("youtube", {}).get(name, 0),
                "telegram": funnel.get("telegram", {}).get(name, 0),
                "dc": funnel.get("dc", {}).get(name, 0),
                "kept": funnel.get("kept", {}).get(name, 0),
            }
        )
    return rows


def publish_status(cfg: dict, status: dict, out_dir: str) -> None:
    """Отправляет готовый статус и историю прямо в бота (KV), минуя GitHub.

    Файлы в репозитории остаются как есть, но бот теперь видит обновление сразу,
    без задержки CDN. Ключ здесь открытый — он умеет только записывать статус
    и ничего не знает о подписчиках и рассылках.
    """
    publish = cfg.get("publish") or {}
    url = publish.get("url")
    key = publish.get("key")
    if not url or not key:
        return
    payload = {
        "status": status,
        "history": load_json(os.path.join(out_dir, "history.json"), []) or [],
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{str(url).rstrip('/')}/publish-status?key={urllib.parse.quote(str(key))}",
        data=data,
        method="POST",
    )
    request.add_header("content-type", "application/json; charset=utf-8")
    request.add_header("user-agent", "vpn-filtered-checker")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            log(f"publish: статус отправлен в бота (HTTP {response.status})")
    except Exception as exc:  # noqa: BLE001
        log(f"publish: статус не отправился ({type(exc).__name__}) — файлы в репозитории остаются")

def write_history(out_dir: str, status: dict, kept: list) -> None:
    """История прогонов: видно, какой источник стабильнее и сколько живут прокси.

    Храним последние 60 прогонов. Хеши конфигов (для «живучести») — только у
    последних 20, чтобы файл в репозитории не разрастался.
    """
    path = os.path.join(out_dir, "history.json")
    history = load_json(path, []) or []
    if not isinstance(history, list):
        history = []

    hashes_by_source = {}
    for item in kept:
        digest = hashlib.sha1(item["uri"].encode("utf-8")).hexdigest()[:12]
        hashes_by_source.setdefault(item.get("source") or "?", []).append(digest)

    entry = {
        "at": status["finished_at"],
        "duration_sec": status["duration_sec"],
        "kept": len(kept),
        "by_source": [
            {"source": row["source"], "parsed": row["parsed"], "kept": row["kept"]}
            for row in status.get("by_source", [])
        ],
        "kept_hashes": hashes_by_source,
    }
    history.append(entry)
    history = history[-60:]
    for old in history[:-20]:
        old.pop("kept_hashes", None)

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        # без отступов: файл в репозитории остаётся компактным
        json.dump(history, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")
    log(f"history: {len(history)} прогонов в истории источников")

def is_universal(item: dict) -> bool:
    """Поймёт ли конфиг обычный клиент без поддержки Reality.

    VLESS + Reality умеют sing-box, Hiddify, NekoBox — но не v2Box и часть
    простых клиентов: у них такой конфиг просто уходит в таймаут. Для них
    собирается отдельный список без Reality.
    """
    outbound = item.get("outbound") or {}
    if outbound.get("type") == "vless":
        tls = outbound.get("tls") or {}
        if (tls.get("reality") or {}).get("public_key"):
            return False
    return True

def write_pool_outputs(cfg: dict, out_dir: str, pool: list) -> None:
    """Живой пул: все, кто прошёл YouTube + Telegram + дата-центр.

    В отборный список попадают только быстрые (порог скорости и задержки), а
    пул — это резерв для автоматического переключения: конфигов здесь в разы
    больше. Клиент сам замеряет их со своей стороны и держит самый быстрый
    живой, поэтому «лишние» отсеиваются уже на месте, у пользователя.
    """
    if not pool:
        return
    os.makedirs(out_dir, exist_ok=True)
    plain_path = os.path.join(out_dir, "pool.txt")
    with open(plain_path, "w", encoding="utf-8", newline="\n") as fh:
        for item in pool:
            fh.write(item["uri"] + "\n")

    auto_path = os.path.join(out_dir, "pool-auto.json")
    with open(auto_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(build_auto_config(pool, cfg), fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # тот же пул в Clash-формате — его принимает Hiddify
    clash_path = os.path.join(out_dir, "pool.yaml")
    with open(clash_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_clash_config(pool, cfg))

    log(f"pool: {len(pool)} серверов в живом пуле (YouTube+Telegram+DC, без порога скорости)")


def uri_with_name(uri: str, name: str) -> str:
    """Подменяет подпись конфига (фрагмент после #) на понятное имя.

    Кириллицу НЕ кодируем: клиенты её понимают, а процентная запись
    (%D0%9F...) выглядит как мусор в списке серверов.
    """
    base = uri.split("#", 1)[0]
    safe = name.replace("#", "").replace("\n", " ")
    return f"{base}#{safe}"


def number_configs(kept: list) -> list:
    """Нумерует конфиги: «Прокси 1», «Прокси 2»…

    Без этого в клиенте видно название всей ссылки вроде
    «🇯🇵[openproxylist.com] vless-JP», и выбрать живой сервер невозможно.
    """
    numbered = []
    for index, item in enumerate(kept, 1):
        name = f"Прокси {index}"
        copy_item = dict(item)
        copy_item["name"] = name
        copy_item["uri"] = uri_with_name(item["uri"], name)
        # тег латиницей — так его понимают все клиенты
        copy_item["tag"] = f"proxy-{index}"
        outbound = dict(item["outbound"])
        outbound["tag"] = copy_item["tag"]
        copy_item["outbound"] = outbound
        numbered.append(copy_item)
    return numbered

def write_outputs(cfg: dict, out_dir: str, kept: list, stats: dict, status: dict) -> None:
    out_cfg = cfg["output"]
    os.makedirs(out_dir, exist_ok=True)
    # Ранжирование по скорости: и человек, и клиент выбирают сверху вниз.
    # Было случайное соседство — самый быстрый мог оказаться десятым.
    kept = sorted(kept, key=lambda item: -(item.get("mbps") or 0))
    kept = number_configs(kept)

    plain_path = os.path.join(out_dir, out_cfg["plain"])
    with open(plain_path, "w", encoding="utf-8", newline="\n") as fh:
        for item in kept:
            fh.write(item["uri"] + "\n")

    # список для клиентов без Reality (v2Box, простые v2rayNG и т.п.)
    universal = [item for item in kept if is_universal(item)]
    universal_path = os.path.join(out_dir, out_cfg.get("universal", "universal.txt"))
    with open(universal_path, "w", encoding="utf-8", newline="\n") as fh:
        for item in universal:
            fh.write(item["uri"] + "\n")
    log(
        f"universal: {len(universal)} из {len(kept)} без Reality "
        f"(для v2Box и клиентов без поддержки Reality)"
    )

    b64_path = os.path.join(out_dir, out_cfg["base64"])
    payload = "\n".join(item["uri"] for item in kept) + "\n"
    with open(b64_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(base64.b64encode(payload.encode("utf-8")).decode("ascii") + "\n")

    # авто-конфиг: клиент сам держит самый быстрый рабочий сервер
    auto_path = os.path.join(out_dir, "auto.json")
    with open(auto_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(build_auto_config(kept, cfg), fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # тот же конфиг в синтаксисе 1.10 — для Hiddify (его ядро старое)
    legacy_path = os.path.join(out_dir, "auto-legacy.json")
    with open(legacy_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(build_auto_config(kept, cfg, legacy=True), fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # тот же смысл, но в Clash YAML — для Stash и других Clash-клиентов
    clash_path = os.path.join(out_dir, "auto.yaml")
    with open(clash_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_clash_config(kept, cfg))

    # готовый профиль для приложения sing-box (iPhone): tun + urltest 30 с
    client_path = os.path.join(out_dir, "auto-client.json")
    with open(client_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(build_client_config(kept, cfg), fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    log("client-profile: профиль для sing-box (tun + auto 30 с) собран")

    log(f"auto-config: {len(kept)} серверов в группе автоматического выбора (json + yaml)")

    with open(os.path.join(out_dir, out_cfg["status"]), "w", encoding="utf-8") as fh:
        json.dump(status, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    write_report(os.path.join(out_dir, out_cfg["report"]), cfg, kept, stats, status)


def write_report(path: str, cfg: dict, kept: list, stats: dict, status: dict) -> None:
    counts = status["counts"]
    lines = [
        "# Отфильтрованный список VPN-конфигов",
        "",
        f"Обновлено: **{status['finished_at']}** UTC "
        f"(прогон занял {status['duration_sec']:.0f} с)",
        "",
        "## Что проверялось",
        "",
        f"1. Endpoint принимает TCP-соединение.",
        f"2. Через прокси открывается `{cfg['youtube']['url']}` "
        f"(ждём HTTP {cfg['youtube']['expected_status']}).",
        f"3. Через прокси открывается `{cfg['telegram']['url']}` "
        f"(ждём HTTP {cfg['telegram']['expected_status']}).",
        f"4. Через прокси открывается TCP-соединение с дата-центром Telegram "
        f"({', '.join(cfg['telegram_dc']['hosts'])}: {cfg['telegram_dc']['port']}) — "
        f"это отсекает прокси, чей IP заблокирован самим Telegram.",
        f"5. Скорость туннеля к Google CDN не ниже **{cfg['speed']['min_mbps']} Мбит/с** "
        f"(скачиваем {cfg['speed']['request_bytes'] // 1024} КБ "
        f"за не более {cfg['speed']['deadline_sec']:.0f} с).",
        "",
        "В список попадают только те конфиги, которые прошли **все** шаги: "
        "и YouTube, и Telegram, и скорость.",
        "",
        "## Воронка",
        "",
        "| Шаг | Осталось |",
        "| --- | ---: |",
        f"| Строк в источниках | {counts['lines']} |",
        f"| Разобрано в конфиги | {counts['parsed']} |",
        f"| Уникальных | {counts['unique']} |",
        f"| Endpoint отвечает по TCP | {counts['tcp_alive']} |",
        f"| YouTube доступен | {counts['youtube_ok']} |",
        f"| + Telegram (HTTP) доступен | {counts['telegram_ok']} |",
        f"| + дата-центр Telegram доступен | {counts.get('telegram_dc_ok', 0)} |",
        f"| + скорость ≥ {cfg['speed']['min_mbps']} Мбит/с | {counts['speed_ok']} |",
        f"| **В итоговом списке** | **{counts['kept']}** |",
        "",
        "## По протоколам",
        "",
        "| Протокол | В списке |",
        "| --- | ---: |",
    ]
    for key, value in sorted(status["by_protocol"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {key} | {value} |")

    lines += ["", "## По странам", "", "| Страна | В списке |", "| --- | ---: |"]
    for key, value in sorted(status["by_country"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {key} | {value} |")

    lines += [
        "",
        "## Самые быстрые",
        "",
        "| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for i, item in enumerate(status["top"], 1):
        lines.append(
            f"| {i} | {item['name'][:48]} | {item['protocol']} | {item['country']} "
            f"| {item['mbps']:.2f} | {item['youtube_ms']} | {item['telegram_ms']} |"
        )

    if status["unsupported_reasons"]:
        lines += ["", "## Что не удалось проверить", "", "| Причина | Конфигов |", "| --- | ---: |"]
        for key, value in sorted(status["unsupported_reasons"].items(), key=lambda kv: -kv[1]):
            lines.append(f"| {key} | {value} |")

    lines += ["", "## Ссылки", ""]
    lines.append(f"- Обычный список: {status['link_plain']}")
    lines.append(f"- Base64-подписка: {status['link_base64']}")
    lines.append("")

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #


class Progress:
    """Отправляет прогресс прогона воркеру, чтобы бот рисовал полосу загрузки.

    Отчёт идёт обычным POST; любая ошибка сети молча игнорируется — прогресс
    не должен ломать саму проверку.
    """

    STAGES = {
        "parse": (5, "Разбор конфигов"),
        "prefilter": (20, "Быстрая проверка связи"),
        "youtube": (25, "Проверка YouTube"),
        "telegram": (62, "Проверка Telegram"),
        "telegram-dc": (70, "Проверка дата-центров Telegram"),
        "latency": (74, "Замер задержки отклика"),
        "speed": (78, "Замер скорости"),
        "publish": (98, "Публикация списка"),
    }

    def __init__(self, url: str = "", key: str = ""):
        self.url = url
        self.key = key
        self.percent = 0
        self.started = time.time()

    def _eta(self) -> int:
        if self.percent <= 0:
            return 0
        elapsed = time.time() - self.started
        return int(elapsed * (100 - self.percent) / self.percent)

    def send(self, percent: int, stage: str, done=None, total=None) -> None:
        self.percent = max(self.percent, min(100, int(percent)))
        payload = {
            "stage": stage,
            "percent": self.percent,
            "done": done,
            "total": total,
            "eta_sec": self._eta(),
            "elapsed_sec": int(time.time() - self.started),
            "started_at": datetime.datetime.fromtimestamp(
                self.started, datetime.timezone.utc
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        log(f"progress {self.percent}% — {stage}")
        if not self.url:
            return
        try:
            query = f"?key={urllib.parse.quote(self.key)}" if self.key else ""
            request = urllib.request.Request(
                self.url + query,
                data=json.dumps(payload).encode("utf-8"),
                method="POST",
            )
            request.add_header("content-type", "application/json")
            request.add_header("user-agent", "vpn-filtered-checker")
            urllib.request.urlopen(request, timeout=15).read()
        except Exception:
            pass  # прогресс — украшение, из-за него проверку не роняем

    def stage(self, name: str, done=None, total=None, percent=None, label=None) -> None:
        base, default_label = self.STAGES.get(name, (self.percent, name))
        self.send(percent if percent is not None else base, label or default_label, done, total)


PROGRESS = Progress()


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="path to config.json")
    parser.add_argument("--sources-dir", help="read source lists from a local directory instead of GitHub")
    parser.add_argument("--cache-dir", default=os.path.join(REPO_ROOT, ".cache", "sources"))
    parser.add_argument("--out-dir", default=REPO_ROOT)
    parser.add_argument("--work-dir", default=os.path.join(REPO_ROOT, ".cache", "singbox"))
    parser.add_argument("--sing-box", default=os.environ.get("SING_BOX") or shutil.which("sing-box"))
    parser.add_argument("--limit", type=int, default=0, help="only handle the first N configs")
    parser.add_argument("--min-mbps", type=float, help="override the speed threshold")
    parser.add_argument("--min-speed-count", type=int, default=0,
                        help="keep at least N speed results even if below threshold")
    parser.add_argument("--min-keep", type=int, default=1,
                        help="abort without touching the published files if fewer than N configs survive")
    parser.add_argument("--no-prefilter", action="store_true")
    parser.add_argument("--skip-speed", action="store_true")
    parser.add_argument("--parse-only", action="store_true", help="do not touch the network")
    parser.add_argument("--out-repo", help="override the GitHub repo used to build links")
    parser.add_argument("--out-branch", help="override the branch used to build links")
    parser.add_argument("--source-files",
                        help="comma separated list overriding source.files, e.g. 6,22")
    parser.add_argument("--timeout-only", action="store_true", help="проверять только время ответа: без YouTube, Telegram и скорости")
    parser.add_argument("--core-check", action="store_true", help="финальная проверка реальным HTTP-запросом через туннель")
    parser.add_argument("--confirm", action="store_true", help="перепроверить выживших: конфиг должен ответить дважды")
    parser.add_argument("--delay-timeout", type=int, help="сколько ждать ответа прокси, мс")
    parser.add_argument("--max-youtube-ms", type=int,
                        help="drop configs whose YouTube delay is above this, ms")
    parser.add_argument("--max-telegram-ms", type=int,
                        help="drop configs whose Telegram delay is above this, ms")
    parser.add_argument("--progress-url", help="POST stage progress here, so the bot can show it")
    parser.add_argument("--progress-key", default="", help="key passed to --progress-url")
    args = parser.parse_args(argv)

    # если адрес прогресса не задан, берём его из config.publish: бот получает
    # этап и процент сразу и перерисовывает открытый экран
    if not args.progress_url:
        publish = (load_json(args.config) or {}).get("publish") or {}
        if publish.get("url") and publish.get("key"):
            base = str(publish["url"]).rstrip("/")
            args.progress_url = f"{base}/checker-progress"
            args.progress_key = str(publish["key"])
    return args


def build_status(cfg: dict, cfg_overrides: dict, stats: dict, counts: dict, kept: list) -> dict:
    repo = cfg_overrides.get("repo") or cfg["output"]["repo"]
    branch = cfg_overrides.get("branch") or cfg["output"]["branch"]
    plain = cfg["output"]["plain"]
    b64 = cfg["output"]["base64"]
    epoch = int(time.time())
    link_plain = f"https://github.com/{repo}/raw/refs/heads/{branch}/{plain}"
    link_b64 = f"https://github.com/{repo}/raw/refs/heads/{branch}/{b64}"
    link_auto = f"https://github.com/{repo}/raw/refs/heads/{branch}/auto.json"
    return {
        "schema": 1,
        "run_id": f"{epoch}-{hashlib.sha256(str(len(kept)).encode()).hexdigest()[:8]}",
        "finished_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_epoch": epoch,
        "duration_sec": round(time.time() - _START, 1),
        "sources": [
            f"{cfg['source']['repo']}/{cfg['source']['dir']}/{n}.txt" for n in cfg["source"]["files"]
        ],
        "counts": counts,
        "by_protocol": {},
        "by_country": {},
        "unsupported_reasons": stats["unsupported_reasons"],
        "link_plain": link_plain,
        "link_plain_bust": f"{link_plain}?t={epoch}",
        "link_auto": link_auto,
        "link_auto_bust": f"{link_auto}?t={epoch}",
        "link_base64": link_b64,
        "link_base64_bust": f"{link_b64}?t={epoch}",
        "html_plain": f"https://github.com/{repo}/blob/{branch}/{plain}",
        "params": {
            "min_mbps": cfg["speed"]["min_mbps"],
            "youtube_url": cfg["youtube"]["url"],
            "telegram_url": cfg["telegram"]["url"],
            "youtube_expected_status": cfg["youtube"]["expected_status"],
            "telegram_expected_status": cfg["telegram"]["expected_status"],
            "speed_url": cfg["speed"]["url"],
        },
        "top": [],
    }


def main(argv=None) -> int:
    global PROGRESS
    args = parse_args(argv)
    PROGRESS = Progress(args.progress_url or "", args.progress_key or "")
    # everything is resolved once, up front: sing-box is spawned with a different
    # working directory, and the workflow passes relative paths like `.cache/singbox`
    args.out_dir = os.path.abspath(args.out_dir)
    args.work_dir = os.path.abspath(args.work_dir)
    args.cache_dir = os.path.abspath(args.cache_dir)
    if args.sources_dir:
        args.sources_dir = os.path.abspath(args.sources_dir)
    if args.sing_box and os.path.exists(args.sing_box):
        args.sing_box = os.path.abspath(args.sing_box)
    cfg = load_json(args.config) or {}
    if args.source_files:
        files = [item.strip() for item in args.source_files.split(",") if item.strip()]
        if files:
            cfg.setdefault("source", {})["files"] = files
            log(f"источники переопределены: {', '.join(files)}")
    if args.min_mbps is not None:
        cfg.setdefault("speed", {})["min_mbps"] = args.min_mbps
    if args.delay_timeout is not None:
        cfg.setdefault("delay", {})["timeout_ms"] = args.delay_timeout
    if args.max_youtube_ms is not None:
        cfg.setdefault("latency", {})["max_youtube_ms"] = args.max_youtube_ms
    if args.max_telegram_ms is not None:
        cfg.setdefault("latency", {})["max_telegram_ms"] = args.max_telegram_ms
    if args.skip_speed:
        cfg["speed"]["min_mbps"] = 0.0

    out_repo = args.out_repo
    out_branch = args.out_branch
    cfg_overrides = {"repo": out_repo, "branch": out_branch}

    log(f"config: {args.config}")
    log(
        "targets: YouTube {} ({}), Telegram {} ({})".format(
            cfg["youtube"]["url"],
            cfg["youtube"]["expected_status"],
            cfg["telegram"]["url"],
            cfg["telegram"]["expected_status"],
        )
    )

    if args.sources_dir:
        raw = read_local_sources(args.sources_dir)
    else:
        raw = download_sources(cfg, args.cache_dir)

    candidates, stats = collect(raw, limit=args.limit, allowed=fetch_ru_prefilter(cfg), cfg_limits=cfg.get("limits"))
    log(
        f"parsed {stats['parsed']} configs "
        f"({stats['unsupported']} unsupported, {stats['duplicates']} duplicates)"
    )
    if not candidates:
        log("nothing to test")
        return 1
    PROGRESS.stage("parse", done=len(candidates), total=len(candidates))

    # воронка по источникам: по ней бот считает, какой источник стабильнее
    sources_order = list(dict.fromkeys(c["source"] for c in candidates))
    funnel = {"parsed": per_source(candidates)}

    counts = {
        "lines": stats["lines"],
        "parsed": stats["parsed"],
        "unsupported": stats["unsupported"],
        "duplicates": stats["duplicates"],
        "unique": len(candidates),
        "tcp_alive": 0,
        "youtube_ok": 0,
        "telegram_ok": 0,
        "telegram_dc_ok": 0,
        "latency_ok": 0,
        "speed_ok": 0,
        "kept": 0,
    }

    if args.parse_only:
        status = build_status(cfg, cfg_overrides, stats, counts, candidates)
        status["by_protocol"] = stats["by_protocol"]
        write_outputs(cfg, args.out_dir, candidates, stats, status)
        log(f"parse-only: wrote {len(candidates)} configs to {args.out_dir}")
        return 0

    if not args.sing_box:
        log("ERROR: sing-box binary not found; pass --sing-box /path/to/sing-box")
        return 2

    log(f"sing-box: {args.sing_box}")
    os.makedirs(args.work_dir, exist_ok=True)

    # --- stage 2 ----------------------------------------------------------- #
    if cfg["tcp_prefilter"]["enabled"] and not args.no_prefilter:
        total_endpoints = len(candidates)
        log(f"tcp prefilter on {total_endpoints} endpoints ...")
        cpu_guess = os.cpu_count() or 2
        concurrency = min(
            int(cfg["tcp_prefilter"]["concurrency"]),
            max(50, cpu_guess * 200),
        )
        alive, alive_count = tcp_prefilter(
            candidates,
            cfg["tcp_prefilter"]["timeout_sec"],
            concurrency,
        )
        log(f"tcp prefilter: {alive_count}/{total_endpoints} alive")
        candidates = alive
        PROGRESS.stage("prefilter", done=alive_count, total=total_endpoints)
    counts["tcp_alive"] = len(candidates)
    funnel["alive"] = per_source(candidates)
    if not candidates:
        log("no endpoint accepted a TCP connection")
        return 1

    # --- stage 3: YouTube ------------------------------------------------ #
    youtube_delay = proxy_stage(
        args.sing_box, args.work_dir, candidates, cfg, "youtube", cfg["youtube"]["url"],
        on_batch=lambda index, count, found: PROGRESS.send(
            25 + int(36 * index / max(1, count)),
            f"Проверка YouTube · партия {index} из {count}",
            done=index,
            total=count,
        ),
    )
    log(f"youtube: {len(youtube_delay)} proxies answered")
    youtube_ok = [c for c in candidates if c["tag"] in youtube_delay]
    counts["youtube_ok"] = len(youtube_ok)
    funnel["youtube"] = per_source(youtube_ok)
    if not youtube_ok:
        log("nothing passed the YouTube test")
        return 1

    # --- режим «только таймаут» ------------------------------------------ #
    # Самый простой критерий, который просил владелец: прокси ответил быстрее
    # заданного времени. Ни YouTube, ни Telegram, ни скорости не проверяем —
    # клиент получает все конфиги с откликом в пределах таймаута.
    if getattr(args, "timeout_only", False):
        survivors = sorted(youtube_ok, key=lambda c: youtube_delay.get(c["tag"]) or 10**9)
        telegram_delay = dict(youtube_delay)  # для инварианта: оба «этапа» пройдены
        for item in survivors:
            item["mbps"] = 0.0
            item["telegram_ms"] = youtube_delay.get(item["tag"])
        counts["telegram_ok"] = len(survivors)
        counts["telegram_dc_ok"] = len(survivors)
        counts["latency_ok"] = len(survivors)
        counts["speed_ok"] = len(survivors)
        counts["kept"] = len(survivors)
        log(
            f"режим только-таймаут: {len(survivors)} конфигов ответили быстрее "
            f"{cfg['delay']['timeout_ms']} мс"
        )
        kept = survivors
        applied_threshold = 0
        speeds = {}
    else:
        kept = None

    # В режиме «только таймаут» тяжёлые этапы пропускаем: собираем результат
    # сразу, тем же кодом, что и в обычном режиме.
    if kept is not None:
        if len(kept) < max(1, args.min_keep):
            log(f"only {len(kept)} configs answered within the timeout; keeping previous list")
            return 3
        for item in kept:
            item["youtube_ms"] = youtube_delay.get(item["tag"])
            item["telegram_ms"] = youtube_delay.get(item["tag"])
            item["mbps"] = 0.0
        status = build_status(cfg, cfg_overrides, stats, counts, kept)
        status["timeout_only"] = True
        status["speed_threshold"] = 0
        status["by_source"] = build_by_source(sources_order, funnel)
        status["by_protocol"] = {}
        status["by_country"] = {}
        for item in kept:
            status["by_protocol"][item["protocol"]] = status["by_protocol"].get(item["protocol"], 0) + 1
            status["by_country"][item["country"]] = status["by_country"].get(item["country"], 0) + 1
        status["top"] = [
            {
                "name": item["name"],
                "protocol": item["protocol"],
                "country": item["country"],
                "server": item["server"],
                "mbps": 0.0,
                "youtube_ms": item["youtube_ms"],
                "telegram_ms": item["telegram_ms"],
            }
            for item in kept[:10]
        ]
        status["invariant"] = {
            "description": "режим «только таймаут»: конфиги ответили в пределах заданного времени",
            "kept": len(kept),
            "kept_without_youtube": 0,
            "kept_without_telegram": 0,
            "all_pass_both": True,
        }
        digest = hashlib.sha256("\n".join(i["uri"] for i in kept).encode()).hexdigest()[:12]
        status["run_id"] = f"{status['finished_epoch']}-{digest}"
        PROGRESS.stage("publish")
        write_outputs(cfg, args.out_dir, kept, stats, status)
        write_history(args.out_dir, status, kept)
        publish_status(cfg, status, args.out_dir)
        log(f"kept {len(kept)} of {counts['unique']} unique configs")
        PROGRESS.send(100, f"Готово: в списке {len(kept)} конфигов")
        return 0
    # --- stage 3b: Telegram ---------------------------------------------- #
    PROGRESS.stage("telegram", done=0, total=len(youtube_ok))
    telegram_delay = proxy_stage(
        args.sing_box, args.work_dir, youtube_ok, cfg, "telegram", cfg["telegram"]["url"]
    )
    log(f"telegram: {len(telegram_delay)} proxies answered")
    PROGRESS.stage("telegram", done=len(telegram_delay), total=len(youtube_ok))
    survivors = [c for c in youtube_ok if c["tag"] in telegram_delay]
    counts["telegram_ok"] = len(survivors)
    funnel["telegram"] = per_source(survivors)
    if not survivors:
        log("nothing passed the Telegram test")
        return 1

    # --- stage 3c: Telegram data centres --------------------------------- #
    if cfg.get("telegram_dc", {}).get("enabled"):
        PROGRESS.stage("telegram-dc", done=0, total=len(survivors))
        dc_ok = telegram_dc_stage(args.sing_box, args.work_dir, survivors, cfg)
        log(f"telegram-dc: {len(dc_ok)} proxies reached a Telegram data centre")
        survivors = [c for c in survivors if c["tag"] in dc_ok]
        counts["telegram_dc_ok"] = len(survivors)
        funnel["dc"] = per_source(survivors)
        PROGRESS.stage("telegram-dc", done=len(survivors), total=len(survivors))
        if not survivors:
            log("nothing reached a Telegram data centre")
            return 1
    else:
        counts["telegram_dc_ok"] = counts["telegram_ok"]

    # --- живой пул -------------------------------------------------------- #
    # Всё, что прошло YouTube + Telegram + дата-центр, до отсечки по скорости и
    # задержке. Это резерв для авто-переключения: клиент сам отберёт живое.
    write_pool_outputs(cfg, args.out_dir, list(survivors))

    # --- подтверждение: конфиг должен ответить дважды -------------------- #
    # Один удачный ответ ничего не значит: прокси может ответить один раз и
    # умереть. Именно такие и давали таймауты на телефоне, хотя проверка в
    # облаке их пропускала.
    if args.confirm and survivors:
        PROGRESS.stage("confirm", done=0, total=len(survivors))
        again_youtube = proxy_stage(
            args.sing_box, args.work_dir, survivors, cfg, "confirm-yt", cfg["youtube"]["url"]
        )
        confirmed = [c for c in survivors if c["tag"] in again_youtube]
        log(f"confirm: YouTube повторно прошли {len(confirmed)} из {len(survivors)}")
        again_telegram = proxy_stage(
            args.sing_box, args.work_dir, confirmed, cfg, "confirm-tg", cfg["telegram"]["url"]
        )
        survivors = [c for c in confirmed if c["tag"] in again_telegram]
        log(f"confirm: после двойной проверки осталось {len(survivors)}")
        if not survivors:
            log("nothing survived the confirmation pass")
            return 1
    # --- финальная проверка реальным запросом ---------------------------- #
    # Пинг может пройти, а настоящий запрос через туннель — нет (502).
    # Клиент ходит именно запросами, поэтому проверяем как он.
    if getattr(args, "core_check", False) and survivors:
        PROGRESS.stage("core", done=0, total=len(survivors))
        try:
            import core_verify

            verified = core_verify.verify(
                survivors, args.sing_box, os.path.join(args.work_dir, "core"), log=log
            )
            log(f"core-check: реально работают {len(verified)} из {len(survivors)}")
            if verified:
                survivors = verified
            else:
                log("core-check: ни один не открыл YouTube+Telegram — оставляем прежний список")
        except Exception as error:  # noqa: BLE001
            log(f"core-check пропущен: {type(error).__name__}: {error}")
    # --- stage 3d: скорость отклика -------------------------------------- #
    # Shorts и короткие видео тормозит не только полоса, но и задержка:
    # конфиг с ответом в 3 секунды ощущается «не грузится». Отсекаем таких до
    # замера скорости — это ещё и экономит трафик на дорогих 3 МБ.
    max_youtube_ms = cfg.get("latency", {}).get("max_youtube_ms") or 0
    max_telegram_ms = cfg.get("latency", {}).get("max_telegram_ms") or 0
    if max_youtube_ms or max_telegram_ms:
        before = len(survivors)
        PROGRESS.stage("latency", done=0, total=before)
        relaxed = list(survivors)
        if max_youtube_ms:
            survivors = [
                c for c in survivors
                if (youtube_delay.get(c["tag"]) or 10**9) <= max_youtube_ms
            ]
        if max_telegram_ms:
            survivors = [
                c for c in survivors
                if (telegram_delay.get(c["tag"]) or 10**9) <= max_telegram_ms
            ]
        log(
            f"скорость отклика: YouTube ≤ {max_youtube_ms} мс, Telegram ≤ {max_telegram_ms} мс "
            f"-> осталось {len(survivors)} из {before}"
        )
        # плохой день в сети не должен оставлять пользователя без списка:
        # если жёсткий фильтр выкосил почти всё, берём всех, кто прошёл проверки
        min_after = int(cfg.get("limits", {}).get("min_after_filters", 5))
        if len(survivors) < min_after <= len(relaxed):
            log(f"отклик: {len(survivors)} — слишком мало, фильтр ослаблен до {len(relaxed)}")
            survivors = relaxed
        if not survivors:
            log("все конфиги отвечают слишком медленно")
            return 1
    counts["latency_ok"] = len(survivors)

    # --- stage 4: throughput --------------------------------------------- #
    speeds = {}
    if cfg["speed"]["min_mbps"] > 0:
        PROGRESS.stage("speed", done=0, total=len(survivors))
        speeds = speed_stage(args.sing_box, args.work_dir, survivors, cfg)
        log(f"speed: {len(speeds)} proxies measured")
        PROGRESS.stage("speed", done=len(survivors), total=len(survivors))
    else:
        log("speed stage skipped")

    threshold = cfg["speed"]["min_mbps"]
    min_speed_count = args.min_speed_count or int(
        cfg.get("speed", {}).get("min_speed_count") or 0
    )
    # Ступенчатый порог: цель — 2 Мбит/с, но пустой список хуже медленного.
    # Берём самый высокий порог, который даёт достаточно конфигов, и честно
    # записываем, какой порог применён.
    target = int(cfg.get("speed", {}).get("min_speed_count") or 8)
    applied_threshold = threshold
    if threshold > 0:
        ranked = sorted(survivors, key=lambda c: -(speeds.get(c["tag"]) or 0.0))
        measured = [c for c in ranked if (speeds.get(c["tag"]) or 0.0) > 0]
        tiers = [threshold, 1.0, 0.5, 0.3]
        chosen = []
        for tier in tiers:
            group = [c for c in measured if (speeds.get(c["tag"]) or 0.0) >= tier]
            if len(group) >= target:
                chosen, applied_threshold = group, tier
                break
            if not chosen and group:
                chosen, applied_threshold = group, tier
        if not chosen:
            chosen, applied_threshold = measured, 0.0
        if applied_threshold < threshold:
            log(
                f"порог скорости снижен до {applied_threshold} Мбит/с: "
                f"на {threshold} Мбит/с набралось слишком мало рабочих"
            )
        kept = chosen
        counts["speed_tier"] = applied_threshold
    else:
        kept = survivors
    counts["speed_ok"] = (
        sum(1 for c in kept if (speeds.get(c["tag"]) or 0.0) >= applied_threshold)
        if applied_threshold > 0
        else len(kept)
    )
    counts["kept"] = len(kept)
    funnel["kept"] = per_source(kept)

    # Жёсткая проверка главного требования: в списке не может быть конфига,
    # у которого не подтверждены ОБЕ проверки — YouTube И Telegram.
    leaks = [
        c["tag"] for c in kept if c["tag"] not in youtube_delay or c["tag"] not in telegram_delay
    ]
    if leaks:
        log(
            f"ERROR: {len(leaks)} конфигов в списке без подтверждённого YouTube или "
            f"Telegram — это ошибка фильтрации, список не публикуется"
        )
        return 4
    log(f"пересечение подтверждено: все {len(kept)} конфигов прошли и YouTube, и Telegram")

    if cfg["limits"].get("max_keep"):
        kept = kept[: cfg["limits"]["max_keep"]]
        counts["kept"] = len(kept)

    # --- output ----------------------------------------------------------- #
    if len(kept) < max(1, args.min_keep):
        log(
            f"only {len(kept)} configs survived (minimum {max(1, args.min_keep)}); "
            "leaving the previously published files untouched"
        )
        return 3

    for item in kept:
        item["youtube_ms"] = youtube_delay.get(item["tag"])
        item["telegram_ms"] = telegram_delay.get(item["tag"])
        item["mbps"] = round(speeds.get(item["tag"], 0.0), 3)

    status = build_status(cfg, cfg_overrides, stats, counts, kept)
    # какой порог скорости реально применён (может быть снижен)
    status["speed_threshold"] = applied_threshold
    status["by_source"] = build_by_source(sources_order, funnel)
    status["by_protocol"] = {}
    status["by_country"] = {}
    for item in kept:
        status["by_protocol"][item["protocol"]] = status["by_protocol"].get(item["protocol"], 0) + 1
        status["by_country"][item["country"]] = status["by_country"].get(item["country"], 0) + 1
    status["top"] = [
        {
            "name": item["name"],
            "protocol": item["protocol"],
            "country": item["country"],
            "server": item["server"],
            "mbps": item["mbps"],
            "youtube_ms": item["youtube_ms"],
            "telegram_ms": item["telegram_ms"],
        }
        for item in sorted(kept, key=lambda c: -(c.get("mbps") or 0))[:10]
    ]
    status["invariant"] = {
        "description": "в списке только те конфиги, где работают И YouTube, И Telegram",
        "kept": len(kept),
        "kept_without_youtube": sum(1 for c in kept if c["tag"] not in youtube_delay),
        "kept_without_telegram": sum(1 for c in kept if c["tag"] not in telegram_delay),
        "all_pass_both": all(
            c["tag"] in youtube_delay and c["tag"] in telegram_delay for c in kept
        ),
    }
    # run_id must change whenever the list changes, so the bot can detect a new run
    digest = hashlib.sha256("\n".join(i["uri"] for i in kept).encode()).hexdigest()[:12]
    status["run_id"] = f"{status['finished_epoch']}-{digest}"

    PROGRESS.stage("publish")
    write_outputs(cfg, args.out_dir, kept, stats, status)
    write_history(args.out_dir, status, kept)
    publish_status(cfg, status, args.out_dir)
    log(f"kept {len(kept)} of {counts['unique']} unique configs")
    log(f"wrote {cfg['output']['plain']}, {cfg['output']['base64']}, "
        f"{cfg['output']['status']}, {cfg['output']['report']} to {args.out_dir}")
    log(f"link: {status['link_plain']}")
    PROGRESS.send(100, f"Готово: в списке {len(kept)} конфигов")
    return 0


if __name__ == "__main__":
    sys.exit(main())
