"""Convert proxy URIs (vless / vmess / trojan / ss / socks / http / hysteria2)
into sing-box outbound dictionaries.

Standard library only: the checker must run on a bare GitHub Actions runner
and on a local Windows box without `pip install`.

Every public function is defensive by design -- a broken or exotic line in the
source subscription must never abort the whole run, it only gets counted as
"unsupported".
"""

from __future__ import annotations

import base64
import binascii
import json
import re
import urllib.parse

# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #

MAX_PORT = 65535

FINGERPRINTS = {
    "chrome",
    "firefox",
    "edge",
    "safari",
    "360",
    "qq",
    "ios",
    "android",
    "random",
    "randomized",
}

# transports sing-box understands; everything else is "unsupported"
WS_TRANSPORTS = {"ws", "websocket"}
GRPC_TRANSPORTS = {"grpc", "gun"}
HTTP_TRANSPORTS = {"h2", "http"}
XHTTP_TRANSPORTS = {"xhttp", "splithttp"}
HTTPUPGRADE_TRANSPORTS = {"httpupgrade"}
DIRECT_TRANSPORTS = {"", "tcp", "raw", "none", "direct"}
UNSUPPORTED_TRANSPORTS = {"quic", "kcp", "mkcp"}


def b64decode_loose(value: str) -> bytes:
    """base64 / base64url decoder that tolerates missing padding."""
    s = (value or "").strip()
    s = s.replace("-", "+").replace("_", "/")
    s = "".join(ch for ch in s if not ch.isspace())
    pad = len(s) % 4
    if pad:
        s += "=" * (4 - pad)
    return base64.b64decode(s, validate=False)


def as_bool(value, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")


def as_port(value):
    try:
        port = int(str(value).strip())
    except Exception:
        return None
    return port if 0 < port <= MAX_PORT else None


def first(params: dict, *names, default=None):
    """Return the first present, non-empty parameter among `names`.

    Values are normally lists (as produced by `parse_qs`), but internally built
    parameter dicts may hold a bare string. Iterating a string would yield single
    characters, so anything that is not a list or tuple is wrapped.
    """
    for name in names:
        if name in params:
            value = params[name]
            candidates = value if isinstance(value, (list, tuple)) else [value]
            for candidate in candidates:
                if candidate is not None and str(candidate).strip() != "":
                    return str(candidate).strip()
    return default


_HOSTNAME_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$")


def looks_like_hostname(value) -> bool:
    """True for values usable as a TLS SNI or an HTTP Host header.

    These mirrors are full of smuggled channel names inside parameters, e.g.
    `?host=/?TELEGRAM--i10VPN` or `?sni=/`. Feeding such junk into an SNI or a
    Host header makes a perfectly working config fail its test, so anything with
    a slash, query mark, `@` or spaces is rejected here.
    """
    if not value:
        return False
    text = str(value).strip()
    if not text or len(text) > 253:
        return False
    return _HOSTNAME_RE.match(text) is not None


def pick_host(params: dict, *names):
    """First parameter value among `names` that actually looks like a hostname."""
    for name in names:
        value = first(params, name)
        if looks_like_hostname(value):
            return value
    return None


def split_host_port(authority: str):
    """Split `host:port`, tolerating IPv6 literals in brackets."""
    authority = authority.strip()
    if authority.startswith("["):  # [2001:db8::1]:443
        end = authority.find("]")
        if end == -1:
            return None, None
        host = authority[1:end]
        rest = authority[end + 1 :]
        if rest.startswith(":"):
            return host, as_port(rest[1:])
        return host, None
    if ":" not in authority:
        return authority, None
    host, _, port = authority.rpartition(":")
    return host, as_port(port)


def normalize_query(query: str) -> str:
    """Some mirrors publish HTML-escaped query strings (`&amp;` instead of `&`).

    Without this the parameter names come out as `amp;pbk` and reality
    configs look like they have no public key.
    """
    return (
        query.replace("&amp;", "&")
        .replace("&#38;", "&")
        .replace("&AMP;", "&")
    )


def split_uri(uri: str):
    """Break a proxy URI into its parts.

    Returns (scheme, userinfo, host, port, params, fragment) or None.
    """
    if "://" not in uri:
        return None
    scheme, rest = uri.split("://", 1)
    scheme = scheme.strip().lower()

    fragment = ""
    if "#" in rest:
        rest, fragment = rest.split("#", 1)
    fragment = urllib.parse.unquote(fragment).strip()

    query = ""
    if "?" in rest:
        rest, query = rest.split("?", 1)

    params = urllib.parse.parse_qs(normalize_query(query), keep_blank_values=True)

    userinfo = ""
    authority = rest.rstrip("/")
    if "@" in authority:
        userinfo, authority = authority.rsplit("@", 1)
    userinfo = urllib.parse.unquote(userinfo)

    host, port = split_host_port(authority)
    if not host:
        return None
    return scheme, userinfo, host.strip(), port, params, fragment


# --------------------------------------------------------------------------- #
# TLS / transport builders
# --------------------------------------------------------------------------- #


def build_utls(fingerprint):
    if not fingerprint:
        return None
    fp = str(fingerprint).strip().lower()
    if fp in ("", "unsafe", "none", "no", "golang"):
        return None
    if fp not in FINGERPRINTS:
        return None
    return {"enabled": True, "fingerprint": fp}


def build_alpn(value):
    if not value:
        return None
    parts = [p.strip() for p in str(value).replace(",", " ").split()]
    return parts or None


def build_tls(params: dict, host: str, *, force: bool = False):
    security = (first(params, "security", default="") or "").lower()
    reality = security == "reality" or as_bool(first(params, "reality"))
    enabled = force or security in ("tls", "reality", "xtls")

    reality_keys = first(params, "pbk", "publicKey", "public_key")
    if reality and not reality_keys:
        # reality without a public key can never complete a handshake
        return None, "reality-without-pbk"

    if not enabled and not reality:
        return None, None

    tls = {"enabled": True}
    # `sni` wins; for plain TLS the `host` parameter is a legitimate fallback
    # (that is what v2rayN does), but for reality `host` is usually a smuggled
    # channel name and reality needs the exact SNI of the target site.
    sni = pick_host(params, "sni", "peer", "servername")
    if sni is None and not reality:
        sni = pick_host(params, "host")
    tls["server_name"] = sni or host
    if as_bool(first(params, "allowInsecure", "insecure", "allow_insecure")):
        tls["insecure"] = True
    alpn = build_alpn(first(params, "alpn"))
    if alpn:
        tls["alpn"] = alpn

    utls = build_utls(first(params, "fp", "fingerprint"))
    if utls:
        tls["utls"] = utls
    elif reality:
        # sing-box refuses to start a reality outbound without uTLS, so configs
        # that carry no `fp` get the common chrome fingerprint
        tls["utls"] = {"enabled": True, "fingerprint": "chrome"}

    if reality:
        reality_cfg = {
            "enabled": True,
            "public_key": reality_keys,
        }
        short_id = first(params, "sid", "shortId", "short_id")
        if short_id:
            reality_cfg["short_id"] = short_id
        tls["reality"] = reality_cfg

    return tls, None


def pick_host_list(params: dict, *names):
    """Like `pick_host`, but accepts a comma separated list of hostnames."""
    for name in names:
        value = first(params, name)
        if not value:
            continue
        parts = [part.strip() for part in value.split(",") if part.strip()]
        if parts and all(looks_like_hostname(part) for part in parts):
            return parts
    return None


def build_transport(params: dict):
    """Return (transport, error)."""
    kind = (first(params, "type", "net", "network", default="") or "").lower()
    path = first(params, "path", "servicePath")
    host_list = pick_host_list(params, "host", "Host")
    host_header = host_list[0] if host_list else None
    # smuggled channel names often sit in `host`; fall back to the real SNI so
    # the request reaches the vhost the server actually serves
    if host_header is None:
        host_header = pick_host(params, "sni", "peer", "servername")
        host_list = [host_header] if host_header else None

    if kind not in KNOWN_TRANSPORT_KINDS:
        # junk in the `type=` parameter (some mirrors publish corrupted lines)
        return None, "transport-unknown"

    if kind in DIRECT_TRANSPORTS:
        # plain TCP: an HTTP headerType with no real transport is bogus anyway
        return None, None
    if kind in UNSUPPORTED_TRANSPORTS:
        return None, f"transport-{kind}"

    if kind in WS_TRANSPORTS:
        ws = {"type": "ws"}
        ws["path"] = path or "/"
        if host_header:
            ws["headers"] = {"Host": host_header}
        early = first(params, "ed", "eh")
        if early:
            try:
                ws["max_early_data"] = int(early)
                ws["early_data_header_name"] = "Sec-WebSocket-Protocol"
            except Exception:
                pass
        return ws, None

    if kind in GRPC_TRANSPORTS:
        service = first(params, "serviceName", "servicename", "path") or ""
        return {"type": "grpc", "service_name": service}, None

    if kind in HTTP_TRANSPORTS:
        http = {"type": "http"}
        if host_list:
            http["host"] = host_list
        if path:
            http["path"] = path
        return http, None

    if kind in HTTPUPGRADE_TRANSPORTS:
        upgrade = {"type": "httpupgrade"}
        if host_header:
            upgrade["host"] = host_header
        if path:
            upgrade["path"] = path
        return upgrade, None

    if kind in XHTTP_TRANSPORTS:
        # sing-box 1.14.3 has no xhttp transport (verified with `sing-box check`)
        return None, "transport-xhttp-unsupported"

    return None, "transport-unknown"


KNOWN_TRANSPORT_KINDS = (
    WS_TRANSPORTS
    | GRPC_TRANSPORTS
    | HTTP_TRANSPORTS
    | XHTTP_TRANSPORTS
    | HTTPUPGRADE_TRANSPORTS
    | DIRECT_TRANSPORTS
    | UNSUPPORTED_TRANSPORTS
)


def build_packet_encoding(params: dict):
    value = (first(params, "packetEncoding", "packet_encoding") or "").lower()
    if value in ("xudp", "packetaddr"):
        return value
    return None


# --------------------------------------------------------------------------- #
# per-protocol parsers
# --------------------------------------------------------------------------- #


def parse_vless(parts, tag):
    scheme, userinfo, host, port, params, fragment = parts
    if not userinfo:
        return None, "vless-without-uuid"
    port = port or as_port(first(params, "port")) or 443
    out = {
        "type": "vless",
        "tag": tag,
        "server": host,
        "server_port": port,
        "uuid": userinfo.split("@")[0],
    }
    encryption = (first(params, "encryption", default="none") or "none").lower()
    if encryption not in ("none", ""):
        return None, "vless-encryption"

    tls, err = build_tls(params, host)
    if err:
        return None, err
    transport, err = build_transport(params)
    if err:
        return None, err

    # sing-box refuses to start on an unknown flow, and Xray's
    # `xtls-rprx-vision-udp443` is just vision with different UDP handling,
    # so it maps onto plain vision instead of killing the whole outbound.
    flow = (first(params, "flow") or "").strip().lower()
    if flow in ("xtls-rprx-vision", "xtls-rprx-vision-udp443"):
        flow = "xtls-rprx-vision"
    else:
        flow = None
    if flow and transport is None and tls and tls.get("enabled"):
        out["flow"] = flow

    packet_encoding = build_packet_encoding(params)
    if packet_encoding:
        out["packet_encoding"] = packet_encoding
    if tls:
        out["tls"] = tls
    if transport:
        out["transport"] = transport
    return out, None


def parse_vmess_uri(uri: str, tag: str):
    """vmess://<base64 json>  or legacy  vmess://<base64 of k=v pairs>."""
    payload = uri.split("://", 1)[1]
    if "#" in payload:
        payload, _ = payload.split("#", 1)
    payload = payload.strip()
    try:
        decoded = b64decode_loose(payload).decode("utf-8", "replace").strip()
    except (binascii.Error, ValueError):
        return None, "vmess-bad-base64"

    if not decoded.startswith("{"):
        return None, "vmess-legacy-format"

    try:
        data = json.loads(decoded)
    except Exception:
        return None, "vmess-bad-json"

    server = str(data.get("add") or "").strip()
    port = as_port(data.get("port"))
    uuid = str(data.get("id") or "").strip()
    if not server or not port or not uuid:
        return None, "vmess-missing-fields"

    security = str(data.get("scy") or data.get("security") or "auto").strip().lower()
    if security not in ("auto", "none", "zero", "aes-128-gcm", "chacha20-poly1305"):
        security = "auto"

    out = {
        "type": "vmess",
        "tag": tag,
        "server": server,
        "server_port": port,
        "uuid": uuid,
        "security": security,
    }
    try:
        out["alter_id"] = int(data.get("aid") or 0)
    except Exception:
        out["alter_id"] = 0

    tls_enabled = str(data.get("tls") or "").strip().lower() in ("tls", "true", "1", "reality")
    params = {}
    if tls_enabled:
        params["security"] = ["tls"]
    for key in ("sni", "alpn", "fp"):
        value = data.get(key)
        if value:
            params[key] = [str(value)]
    if data.get("allowInsecure") or data.get("insecure"):
        params["allowInsecure"] = ["1"]

    tls, err = build_tls(params, server)
    if err:
        return None, err

    net = str(data.get("net") or "tcp").strip().lower()
    fake = {
        "type": [net],
        "path": [str(data.get("path") or "")],
        "host": [str(data.get("host") or "")],
        "serviceName": [str(data.get("path") or "")],
    }
    if str(data.get("type") or "").strip().lower() in ("http",) and net == "tcp":
        return None, "vmess-http-obfs"
    transport, err = build_transport(fake)
    if err:
        return None, err

    if tls:
        out["tls"] = tls
    if transport:
        out["transport"] = transport
    header_type = str(data.get("type") or "").strip().lower()
    if net in ("ws", "tcp") and header_type not in ("", "none", "http"):
        # exotic header obfuscation we cannot reproduce
        return None, "vmess-header-type"
    return out, None


def parse_trojan(parts, tag):
    scheme, userinfo, host, port, params, fragment = parts
    if not userinfo:
        return None, "trojan-without-password"
    port = port or 443
    password = userinfo
    params = dict(params)
    params.setdefault("security", ["tls"])
    tls, err = build_tls(params, host, force=True)
    if err:
        return None, err
    transport, err = build_transport(params)
    if err:
        return None, err
    out = {
        "type": "trojan",
        "tag": tag,
        "server": host,
        "server_port": port,
        "password": password,
        "tls": tls,
    }
    if transport:
        out["transport"] = transport
    return out, None


SS_METHODS = {
    "aes-128-gcm",
    "aes-192-gcm",
    "aes-256-gcm",
    "aes-128-cfb",
    "aes-192-cfb",
    "aes-256-cfb",
    "aes-128-ctr",
    "aes-192-ctr",
    "aes-256-ctr",
    "chacha20-ietf-poly1305",
    "xchacha20-ietf-poly1305",
    "chacha20-ietf",
    "chacha20",
    "2022-blake3-aes-128-gcm",
    "2022-blake3-aes-256-gcm",
    "2022-blake3-chacha20-poly1305",
    "none",
    "rc4-md5",
}


SS2022_KEY_BYTES = {
    "2022-blake3-aes-128-gcm": 16,
    "2022-blake3-aes-256-gcm": 32,
    "2022-blake3-chacha20-poly1305": 32,
}


def ss2022_key_problem(method, password):
    """Return a reason when a Shadowsocks 2022 key would not load in sing-box."""
    expected = SS2022_KEY_BYTES.get(method)
    if expected is None:
        return None
    parts = str(password or "").split(":") or [""]
    for part in parts:
        try:
            raw = base64.b64decode(part.strip(), validate=True)
        except (binascii.Error, ValueError):
            return "ss-2022-bad-key"
        if len(raw) != expected:
            return "ss-2022-bad-key"
    return None


def _ss_outbound(method, password, host, port, tag, params):
    method = (method or "").strip().lower()
    if method not in SS_METHODS:
        return None, f"ss-method-{method or 'unknown'}"
    problem = ss2022_key_problem(method, password)
    if problem:
        return None, problem
    if not host or not port:
        return None, "ss-missing-host"
    if method == "none" and not password:
        return None, "ss-no-password"
    out = {
        "type": "shadowsocks",
        "tag": tag,
        "server": host,
        "server_port": port,
        "method": method,
        "password": password or "",
    }
    plugin = first(params, "plugin")
    if plugin:
        plugin = urllib.parse.unquote(plugin)
        name, _, opts = plugin.partition(";")
        name = name.strip().lower()
        options = {}
        for chunk in opts.split(";"):
            if "=" in chunk:
                key, _, value = chunk.partition("=")
                options[key.strip()] = value.strip()
        if name in ("obfs-local", "simple-obfs", "obfs"):
            # sing-box 1.14.3 ships no `obfs` plugin, so these can never connect
            return None, "ss-plugin-obfs"
        elif name == "v2ray-plugin":
            out["plugin"] = "v2ray-plugin"
            out["plugin_opts"] = opts.strip()
        else:
            return None, f"ss-plugin-{name}"
    return out, None


def parse_ss(uri: str, tag: str):
    payload = uri.split("://", 1)[1]
    fragment = ""
    if "#" in payload:
        payload, fragment = payload.split("#", 1)
    query = ""
    if "?" in payload:
        payload, query = payload.split("?", 1)
    params = urllib.parse.parse_qs(normalize_query(query), keep_blank_values=True)

    host = port = None
    method = password = None
    if "@" in payload:
        # SIP002: ss://base64(method:password)@host:port
        credentials, _, authority = payload.rpartition("@")
        try:
            decoded = b64decode_loose(credentials).decode("utf-8", "replace")
        except (binascii.Error, ValueError):
            decoded = urllib.parse.unquote(credentials)
        if ":" not in decoded:
            return None, "ss-bad-credentials"
        method, _, password = decoded.partition(":")
        host, port = split_host_port(urllib.parse.unquote(authority))
    else:
        try:
            decoded = b64decode_loose(payload).decode("utf-8", "replace")
        except (binascii.Error, ValueError):
            return None, "ss-bad-base64"
        if "@" not in decoded or ":" not in decoded:
            return None, "ss-legacy-bad"
        credentials, _, authority = decoded.rpartition("@")
        method, _, password = credentials.partition(":")
        host, port = split_host_port(authority)

    return _ss_outbound(method, password, host, port, tag, params)


def parse_socks(parts, tag):
    scheme, userinfo, host, port, params, fragment = parts
    port = port or 1080
    if not host:
        return None, "socks-missing-host"
    out = {
        "type": "socks",
        "tag": tag,
        "server": host,
        "server_port": port,
        "version": "5",
    }
    if userinfo and ":" in userinfo:
        username, _, password = userinfo.partition(":")
        if username:
            out["username"] = username
            out["password"] = password
    return out, None


def parse_http(parts, tag, secure_hint=False):
    scheme, userinfo, host, port, params, fragment = parts
    port = port or (443 if secure_hint else 80)
    if not host:
        return None, "http-missing-host"
    out = {"type": "http", "tag": tag, "server": host, "server_port": port}
    if userinfo and ":" in userinfo:
        username, _, password = userinfo.partition(":")
        if username and username.lower() not in ("none", "null"):
            out["username"] = username
            out["password"] = password
    if secure_hint or scheme == "https":
        tls = {"enabled": True}
        sni = first(params, "sni", "host") or host
        if sni:
            tls["server_name"] = sni
        if as_bool(first(params, "allowInsecure", "insecure")):
            tls["insecure"] = True
        out["tls"] = tls
    return out, None


def parse_hysteria2(parts, tag):
    scheme, userinfo, host, port, params, fragment = parts
    if not host or not port:
        return None, "hy2-missing-host"
    if not userinfo:
        return None, "hy2-without-password"
    password = urllib.parse.unquote(userinfo)
    tls, err = build_tls(params, host, force=True)
    if err:
        return None, err
    out = {
        "type": "hysteria2",
        "tag": tag,
        "server": host,
        "server_port": port,
        "password": password,
        "tls": tls or {"enabled": True, "server_name": host},
    }
    obfs = first(params, "obfs")
    obfs_password = first(params, "obfs-password", "obfs_password")
    if obfs:
        if obfs.lower() != "salamander":
            return None, f"hy2-obfs-{obfs}"
        if not obfs_password:
            return None, "hy2-obfs-without-password"
        out["obfs"] = {"type": "salamander", "password": obfs_password}
    return out, None


def parse_tuic(parts, tag):
    scheme, userinfo, host, port, params, fragment = parts
    if not host or not port:
        return None, "tuic-missing-host"
    if ":" not in userinfo:
        return None, "tuic-without-password"
    uuid, _, password = userinfo.partition(":")
    uuid = uuid.strip()
    password = urllib.parse.unquote(password.strip())
    if not uuid or not password:
        return None, "tuic-without-password"
    tls, err = build_tls(params, host, force=True)
    if err:
        return None, err
    alpn = first(params, "alpn")
    if not alpn:
        tls = dict(tls or {})
        tls["enabled"] = True
        tls.setdefault("server_name", host)
        tls.setdefault("alpn", ["h3"])
    out = {
        "type": "tuic",
        "tag": tag,
        "server": host,
        "server_port": port,
        "uuid": uuid,
        "password": password,
        "tls": tls or {"enabled": True, "server_name": host, "alpn": ["h3"]},
    }
    congestion = first(params, "congestion_control", "congestion-control")
    if congestion:
        out["congestion_control"] = congestion
    relay = first(params, "udp_relay_mode", "udp-relay-mode")
    if relay:
        out["udp_relay_mode"] = relay
    return out, None


# --------------------------------------------------------------------------- #
# entry point
# --------------------------------------------------------------------------- #

SUPPORTED_SCHEMES = (
    "vless",
    "vmess",
    "trojan",
    "ss",
    "socks5",
    "socks",
    "socks4",
    "http",
    "https",
    "hysteria2",
    "hy2",
    "tuic",
)


def parse_uri(uri: str, tag: str):
    """Convert one URI into a sing-box outbound.

    Returns (outbound_dict, None) on success or (None, reason) otherwise.
    """
    uri = (uri or "").strip()
    if not uri:
        return None, "empty"
    scheme = uri.split("://", 1)[0].strip().lower() if "://" in uri else ""
    if scheme not in SUPPORTED_SCHEMES:
        return None, f"scheme-{scheme or 'unknown'}"
    if scheme in ("socks4",):
        return None, "socks4-unsupported"

    if scheme == "vmess":
        return parse_vmess_uri(uri, tag)
    if scheme == "ss":
        return parse_ss(uri, tag)

    parts = split_uri(uri)
    if parts is None:
        return None, "unparsable"

    if scheme == "vless":
        return parse_vless(parts, tag)
    if scheme == "trojan":
        return parse_trojan(parts, tag)
    if scheme in ("socks5", "socks"):
        return parse_socks(parts, tag)
    if scheme in ("http", "https"):
        return parse_http(parts, tag, secure_hint=(scheme == "https"))
    if scheme in ("hysteria2", "hy2"):
        return parse_hysteria2(parts, tag)
    if scheme == "tuic":
        return parse_tuic(parts, tag)
    return None, f"scheme-{scheme}"


def uri_name(uri: str) -> str:
    """Human readable name from the URI fragment."""
    if "#" not in uri:
        return ""
    return urllib.parse.unquote(uri.split("#", 1)[1]).strip()


def uri_endpoint(uri: str):
    """Return (host, port) for a URI, used by the TCP pre-filter."""
    scheme = uri.split("://", 1)[0].strip().lower() if "://" in uri else ""
    try:
        if scheme == "vmess":
            payload = uri.split("://", 1)[1]
            if "#" in payload:
                payload, _ = payload.split("#", 1)
            data = json.loads(b64decode_loose(payload).decode("utf-8", "replace"))
            return str(data.get("add") or "").strip(), as_port(data.get("port"))
        if scheme == "ss":
            out, _ = parse_ss(uri, "probe")
            if out:
                return out["server"], out["server_port"]
            return None, None
        parts = split_uri(uri)
        if parts is None:
            return None, None
        _, _, host, port, params, _ = parts
        if port is None:
            port = as_port(first(params, "port"))
        if port is None:
            port = {"http": 80, "https": 443, "socks5": 1080, "socks": 1080}.get(scheme)
        return host, port
    except Exception:
        return None, None


def uri_server(uri: str) -> str:
    host, _ = uri_endpoint(uri)
    return host or ""


def dedupe_key(uri: str) -> str:
    """Stable identity of a config, ignoring its display name."""
    return uri.split("#", 1)[0].strip().lower()
