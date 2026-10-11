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
    src = cfg["source"]
    urls = {}
    out = {}
    for name in src["files"]:
        url = (
            f"https://raw.githubusercontent.com/{src['repo']}/refs/heads/"
            f"{src['ref']}/{src['dir']}/{name}.txt"
        )
        urls[name] = url
        cached = os.path.join(cache_dir, f"{name}.txt")
        if os.path.exists(cached) and os.path.getsize(cached) > 0:
            with open(cached, "rb") as fh:
                out[name] = fh.read()
            log(f"source {name}.txt: {len(out[name])} bytes (cached)")
            continue
        data = http_get(url)
        os.makedirs(cache_dir, exist_ok=True)
        with open(cached, "wb") as fh:
            fh.write(data)
        out[name] = data
        log(f"source {name}.txt: {len(data)} bytes")
    return out


def read_local_sources(directory: str) -> dict:
    out = {}
    for name in sorted(os.listdir(directory)):
        if name.endswith(".txt"):
            with open(os.path.join(directory, name), "rb") as fh:
                out[name[:-4]] = fh.read()
    return out


def collect(raw_sources: dict, limit: int = 0):
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
        for raw in text.splitlines():
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
    results: dict, stats: dict
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
            stats["drops"] += 1
            log(f"{stage}: dropping 1 config ({group[0]['name'][:36]!r}): {str(exc)[:110]}")
            return
        middle = len(group) // 2
        log(f"{stage}: group of {len(group)} would not start, splitting: {str(exc)[:90]}")
        _delay_group(binary, workdir, group[:middle], cfg, stage, url, results, stats)
        _delay_group(binary, workdir, group[middle:], cfg, stage, url, results, stats)
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


def proxy_stage(binary: str, workdir: str, candidates: list, cfg: dict, stage: str, url: str) -> dict:
    """Run the delay probe for every candidate, in batches. Returns {tag: delay}."""
    results = {}
    stats = {"drops": 0}
    batch_size = cfg["delay"]["batch_size"]
    budget = cfg["limits"].get("time_budget_sec", 0)
    drop_limit = max(25, int(0.05 * len(candidates)))

    batches = [candidates[i : i + batch_size] for i in range(0, len(candidates), batch_size)]
    log(f"{stage}: {len(candidates)} proxies in {len(batches)} batches")

    for index, batch in enumerate(batches, 1):
        if budget and time.time() - _START > budget:
            log(f"{stage}: time budget exhausted after batch {index - 1}")
            break
        before = len(results)
        _delay_group(binary, workdir, batch, cfg, stage, url, results, stats)
        log(f"{stage}: batch {index}/{len(batches)} -> +{len(results) - before}, total {len(results)}")
        if stats["drops"] > drop_limit:
            raise RuntimeError(
                f"{stage}: {stats['drops']} конфигов подряд не дали sing-box стартовать "
                f"(порог {drop_limit}) — это похоже на системную проблему, а не на битые "
                f"конфиги. Прогон остановлен, чтобы не молотить впустую."
            )

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


def _speed_group(binary: str, workdir: str, group: list, cfg: dict, results: dict, stats: dict) -> None:
    """Measure throughput for one group, one local proxy port per config."""
    speed_cfg = cfg["speed"]
    url = speed_cfg["url"]
    request_bytes = speed_cfg["request_bytes"]
    deadline = speed_cfg["deadline_sec"]

    ports = allocate_ports(len(group))
    api_port = free_port()
    config = base_config(group[0]["tag"])
    config["outbounds"] = [c["outbound"] for c in group]
    config["inbounds"] = [
        {"type": "mixed", "tag": f"in{i:04d}", "listen": "127.0.0.1", "listen_port": port}
        for i, port in enumerate(ports)
    ]
    config["route"]["rules"] = [
        {"inbound": [f"in{i:04d}"], "outbound": c["tag"]} for i, c in enumerate(group)
    ]

    instance = SingBox(binary, workdir, f"speed-{next(_INSTANCE_SEQ):04d}")
    try:
        instance.start(config, api_port)
    except Exception as exc:  # noqa: BLE001
        instance.stop()
        if len(group) == 1:
            stats["drops"] += 1
            log(f"speed: dropping 1 config ({group[0]['name'][:36]!r}): {str(exc)[:110]}")
            return
        middle = len(group) // 2
        log(f"speed: group of {len(group)} would not start, splitting: {str(exc)[:90]}")
        _speed_group(binary, workdir, group[:middle], cfg, results, stats)
        _speed_group(binary, workdir, group[middle:], cfg, results, stats)
        return

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(group)) as pool:
            futures = {
                pool.submit(throughput_probe, port, url, request_bytes, deadline): candidate
                for port, candidate in zip(ports, group)
            }
            for future in concurrent.futures.as_completed(futures):
                candidate = futures[future]
                try:
                    _got, mbps, _error = future.result()
                except Exception:  # noqa: BLE001
                    mbps = None
                if mbps:
                    results[candidate["tag"]] = mbps
    finally:
        instance.stop()


def speed_stage(binary: str, workdir: str, candidates: list, cfg: dict) -> dict:
    min_mbps = cfg["speed"]["min_mbps"]
    concurrency = cfg["speed"]["concurrency"]
    budget = cfg["limits"].get("time_budget_sec", 0)

    results = {}
    stats = {"drops": 0}
    drop_limit = max(25, int(0.05 * len(candidates)))
    chunks = [candidates[i : i + concurrency] for i in range(0, len(candidates), concurrency)]
    log(f"speed: {len(candidates)} proxies in {len(chunks)} chunks (>= {min_mbps} Mbit/s)")

    for index, chunk in enumerate(chunks, 1):
        if budget and time.time() - _START > budget:
            log(f"speed: time budget exhausted after chunk {index - 1}")
            break
        before = len(results)
        _speed_group(binary, workdir, chunk, cfg, results, stats)
        passed = sum(1 for v in results.values() if v >= min_mbps)
        log(
            f"speed: chunk {index}/{len(chunks)} -> +{len(results) - before} measured, "
            f"{passed} at or above threshold"
        )
        if stats["drops"] > drop_limit:
            raise RuntimeError(
                f"speed: {stats['drops']} конфигов подряд не дали sing-box стартовать "
                f"(порог {drop_limit}) — похоже на системную проблему. Прогон остановлен."
            )

    return results


# --------------------------------------------------------------------------- #
# output
# --------------------------------------------------------------------------- #


def write_outputs(cfg: dict, out_dir: str, kept: list, stats: dict, status: dict) -> None:
    out_cfg = cfg["output"]
    os.makedirs(out_dir, exist_ok=True)

    plain_path = os.path.join(out_dir, out_cfg["plain"])
    with open(plain_path, "w", encoding="utf-8", newline="\n") as fh:
        for item in kept:
            fh.write(item["uri"] + "\n")

    b64_path = os.path.join(out_dir, out_cfg["base64"])
    payload = "\n".join(item["uri"] for item in kept) + "\n"
    with open(b64_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(base64.b64encode(payload.encode("utf-8")).decode("ascii") + "\n")

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
        f"4. Скорость туннеля к Google CDN не ниже **{cfg['speed']['min_mbps']} Мбит/с** "
        f"(скачиваем {cfg['speed']['request_bytes'] // 1024} КБ "
        f"за не более {cfg['speed']['deadline_sec']:.0f} с).",
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
        f"| Telegram доступен | {counts['telegram_ok']} |",
        f"| Скорость ≥ {cfg['speed']['min_mbps']} Мбит/с | {counts['speed_ok']} |",
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
    return parser.parse_args(argv)


def build_status(cfg: dict, cfg_overrides: dict, stats: dict, counts: dict, kept: list) -> dict:
    repo = cfg_overrides.get("repo") or cfg["output"]["repo"]
    branch = cfg_overrides.get("branch") or cfg["output"]["branch"]
    plain = cfg["output"]["plain"]
    b64 = cfg["output"]["base64"]
    epoch = int(time.time())
    link_plain = f"https://github.com/{repo}/raw/refs/heads/{branch}/{plain}"
    link_b64 = f"https://github.com/{repo}/raw/refs/heads/{branch}/{b64}"
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
    args = parse_args(argv)
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
    if args.min_mbps is not None:
        cfg.setdefault("speed", {})["min_mbps"] = args.min_mbps
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

    candidates, stats = collect(raw, limit=args.limit)
    log(
        f"parsed {stats['parsed']} configs "
        f"({stats['unsupported']} unsupported, {stats['duplicates']} duplicates)"
    )
    if not candidates:
        log("nothing to test")
        return 1

    counts = {
        "lines": stats["lines"],
        "parsed": stats["parsed"],
        "unsupported": stats["unsupported"],
        "duplicates": stats["duplicates"],
        "unique": len(candidates),
        "tcp_alive": 0,
        "youtube_ok": 0,
        "telegram_ok": 0,
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
        log(f"tcp prefilter on {len(candidates)} endpoints ...")
        alive, alive_count = tcp_prefilter(
            candidates,
            cfg["tcp_prefilter"]["timeout_sec"],
            cfg["tcp_prefilter"]["concurrency"],
        )
        log(f"tcp prefilter: {alive_count}/{len(candidates)} alive")
        candidates = alive
    counts["tcp_alive"] = len(candidates)
    if not candidates:
        log("no endpoint accepted a TCP connection")
        return 1

    # --- stage 3: YouTube ------------------------------------------------ #
    youtube_delay = proxy_stage(
        args.sing_box, args.work_dir, candidates, cfg, "youtube", cfg["youtube"]["url"]
    )
    log(f"youtube: {len(youtube_delay)} proxies answered")
    youtube_ok = [c for c in candidates if c["tag"] in youtube_delay]
    counts["youtube_ok"] = len(youtube_ok)
    if not youtube_ok:
        log("nothing passed the YouTube test")
        return 1

    # --- stage 3b: Telegram ---------------------------------------------- #
    telegram_delay = proxy_stage(
        args.sing_box, args.work_dir, youtube_ok, cfg, "telegram", cfg["telegram"]["url"]
    )
    log(f"telegram: {len(telegram_delay)} proxies answered")
    survivors = [c for c in youtube_ok if c["tag"] in telegram_delay]
    counts["telegram_ok"] = len(survivors)
    if not survivors:
        log("nothing passed the Telegram test")
        return 1

    # --- stage 4: throughput --------------------------------------------- #
    speeds = {}
    if cfg["speed"]["min_mbps"] > 0:
        speeds = speed_stage(args.sing_box, args.work_dir, survivors, cfg)
        log(f"speed: {len(speeds)} proxies measured")
    else:
        log("speed stage skipped")

    threshold = cfg["speed"]["min_mbps"]
    if threshold > 0:
        # best-effort top-up so a slow day does not empty the list entirely
        ranked = sorted(survivors, key=lambda c: -(speeds.get(c["tag"]) or 0.0))
        passed = [c for c in ranked if (speeds.get(c["tag"]) or 0.0) >= threshold]
        if args.min_speed_count and len(passed) < args.min_speed_count:
            extra = [c for c in ranked if c not in passed][: args.min_speed_count - len(passed)]
            passed.extend(extra)
            log(f"topped up to {len(passed)} with slower proxies")
        kept = passed
    else:
        kept = survivors
    counts["speed_ok"] = (
        sum(1 for c in kept if (speeds.get(c["tag"]) or 0.0) >= threshold) if threshold > 0 else 0
    )
    counts["kept"] = len(kept)

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
    # run_id must change whenever the list changes, so the bot can detect a new run
    digest = hashlib.sha256("\n".join(i["uri"] for i in kept).encode()).hexdigest()[:12]
    status["run_id"] = f"{status['finished_epoch']}-{digest}"

    write_outputs(cfg, args.out_dir, kept, stats, status)
    log(f"kept {len(kept)} of {counts['unique']} unique configs")
    log(f"wrote {cfg['output']['plain']}, {cfg['output']['base64']}, "
        f"{cfg['output']['status']}, {cfg['output']['report']} to {args.out_dir}")
    log(f"link: {status['link_plain']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
