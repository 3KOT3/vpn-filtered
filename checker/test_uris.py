"""Unit tests for the URI -> sing-box converter.

No network access is needed, so these run anywhere:

    python -m unittest discover -s checker -v
"""

import base64
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uris  # noqa: E402


def b64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def vmess(json_payload: dict) -> str:
    return "vmess://" + b64(json.dumps(json_payload))


class VlessTests(unittest.TestCase):
    def test_html_escaped_query_and_junk_host(self):
        """`&amp;` must be unescaped, and a smuggled `host` must not become the SNI."""
        uri = (
            "vless://9c3f61dc-ab33-48d3-b829-bc1cad0f31f7@34.35.11.97:24822"
            "?security=reality&amp;encryption=none"
            "&amp;pbk=tZ1ioVafOFT_0m30INlvEDNFSj6tcNnG21aJQRy3zVo"
            "&amp;host=%2F%3FBIA_TELEGRAM_MARAMBASHI&amp;headerType=none"
            "&amp;fp=qq&amp;type=tcp&amp;flow=xtls-rprx-vision#%5BOpenRay%5D"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["server"], "34.35.11.97")
        self.assertEqual(out["server_port"], 24822)
        self.assertEqual(out["flow"], "xtls-rprx-vision")
        self.assertEqual(
            out["tls"]["reality"]["public_key"],
            "tZ1ioVafOFT_0m30INlvEDNFSj6tcNnG21aJQRy3zVo",
        )
        # junk host must be ignored, the server address is the SNI
        self.assertEqual(out["tls"]["server_name"], "34.35.11.97")
        self.assertEqual(out["tls"]["utls"]["fingerprint"], "qq")
        self.assertNotIn("transport", out)

    def test_trailing_slash_after_port(self):
        uri = (
            "vless://e75ad2eb-6c1f-45ce-8023-f5f10875df66@185.104.63.173:443/"
            "?type=tcp&security=reality&pbk=AAA&sni=zsat.eu-cdn294.com#x"
        )
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["server_port"], 443)

        uri = (
            "vless://e75ad2eb-6c1f-45ce-8023-f5f10875df66@1.2.3.4:21033/"
            "?security=reality&pbk=AAA&sni=a.b#x"
        )
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["server_port"], 21033)

    def test_reality_without_fingerprint_gets_chrome(self):
        uri = "vless://u@1.2.3.4:443?security=reality&pbk=AAA&sni=a.b&type=tcp#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["tls"]["utls"]["fingerprint"], "chrome")

    def test_reality_without_public_key(self):
        uri = "vless://u@1.2.3.4:443?security=reality&sni=a.b&type=tcp#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "reality-without-pbk")

    def test_ws_early_data_and_host_header(self):
        uri = "vless://u@1.2.3.4:443?type=ws&path=%2Fvl&host=a.b&ed=2048&security=tls#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["transport"]["type"], "ws")
        self.assertEqual(out["transport"]["path"], "/vl")
        self.assertEqual(out["transport"]["headers"], {"Host": "a.b"})
        self.assertEqual(out["transport"]["max_early_data"], 2048)
        self.assertEqual(
            out["transport"]["early_data_header_name"], "Sec-WebSocket-Protocol"
        )

    def test_host_used_as_sni_for_plain_tls(self):
        uri = "vless://u@1.2.3.4:443?security=tls&type=ws&host=x.m-90.xyz&path=/a#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["tls"]["server_name"], "x.m-90.xyz")

    def test_flow_dropped_on_websocket(self):
        uri = "vless://u@1.2.3.4:443?type=ws&path=/&flow=xtls-rprx-vision&security=tls#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertNotIn("flow", out)

    def test_httpupgrade_supported(self):
        uri = "vless://u@1.2.3.4:443?type=httpupgrade&path=/&host=a.b&security=tls#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["transport"]["type"], "httpupgrade")

    def test_xhttp_unsupported(self):
        uri = "vless://u@1.2.3.4:443?type=xhttp&security=tls&path=/&mode=auto#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "transport-xhttp-unsupported")

    def test_mlkem_encryption_unsupported(self):
        uri = "vless://u@1.2.3.4:443?encryption=mlkem768x25519plus.native.0rtt.ABC#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "vless-encryption")

    def test_packet_encoding(self):
        uri = "vless://u@1.2.3.4:443?security=tls&type=ws&path=/&packetEncoding=xudp#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["packet_encoding"], "xudp")

    def test_corrupted_type_parameter(self):
        uri = "vless://u@1.2.3.4:443?type=tcp%233%40oneclickvpnkeys#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "transport-unknown")

    def test_xray_udp443_flow_maps_to_vision(self):
        """sing-box aborts the whole config on an unknown flow value."""
        uri = (
            "vless://u@1.2.3.4:443?security=reality&pbk=AAA&sni=a.b&type=tcp"
            "&flow=xtls-rprx-vision-udp443#x"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["flow"], "xtls-rprx-vision")

    def test_unknown_flow_is_dropped(self):
        uri = (
            "vless://u@1.2.3.4:443?security=reality&pbk=AAA&sni=a.b&type=tcp"
            "&flow=xtls-rprx-direct#x"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertNotIn("flow", out)


class VmessTests(unittest.TestCase):
    def test_plain_url_json(self):
        uri = vmess(
            {
                "v": "2",
                "ps": "test",
                "add": "1.2.3.4",
                "port": "443",
                "id": "e75ad2eb-6c1f-45ce-8023-f5f10875df66",
                "aid": "0",
                "scy": "auto",
                "net": "ws",
                "type": "none",
                "host": "a.b",
                "path": "/ws",
                "tls": "tls",
                "sni": "a.b",
            }
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "vmess")
        self.assertEqual(out["server"], "1.2.3.4")
        self.assertEqual(out["server_port"], 443)
        self.assertEqual(out["alter_id"], 0)
        self.assertEqual(out["transport"]["path"], "/ws")
        self.assertTrue(out["tls"]["enabled"])
        self.assertEqual(out["tls"]["server_name"], "a.b")

    def test_base64url_without_padding(self):
        payload = json.dumps(
            {"add": "1.2.3.4", "port": 443, "id": "u", "net": "tcp", "tls": ""}
        ).encode()
        encoded = base64.urlsafe_b64encode(payload).decode().rstrip("=")
        out, reason = uris.parse_uri("vmess://" + encoded, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["server"], "1.2.3.4")

    def test_legacy_format_rejected(self):
        uri = "vmess://" + b64("auto:aes-128-gcm:uuid@1.2.3.4:443")
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "vmess-legacy-format")

    def test_http_header_obfuscation_rejected(self):
        uri = vmess(
            {"add": "1.2.3.4", "port": "443", "id": "u", "net": "tcp", "type": "http"}
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "vmess-http-obfs")


class ShadowsocksTests(unittest.TestCase):
    def test_sip002(self):
        creds = b64("aes-128-gcm:85590bd2-807b-49b9-af20-1101c18b9eda")
        uri = f"ss://{creds}@ruot.ayucloudservices.nl:40022#%5BOpenRay%5D"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "shadowsocks")
        self.assertEqual(out["method"], "aes-128-gcm")
        self.assertEqual(out["password"], "85590bd2-807b-49b9-af20-1101c18b9eda")
        self.assertEqual(out["server"], "ruot.ayucloudservices.nl")
        self.assertEqual(out["server_port"], 40022)

    def test_legacy(self):
        uri = "ss://" + b64("aes-256-gcm:secret@1.2.3.4:8388") + "#name"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["method"], "aes-256-gcm")
        self.assertEqual(out["password"], "secret")
        self.assertEqual(out["server_port"], 8388)

    def test_2022_method(self):
        uri = "ss://" + b64("2022-blake3-aes-128-gcm:AAAAAAAAAAAAAAAAAAAAAA==@1.2.3.4:443") + "#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["method"], "2022-blake3-aes-128-gcm")

    def test_2022_wrong_key_length_rejected(self):
        """A plain-text password for a 2022 cipher makes sing-box refuse to start."""
        uri = "ss://" + b64("2022-blake3-aes-128-gcm:plainpassword@1.2.3.4:443") + "#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "ss-2022-bad-key")

    def test_2022_multiuser_keys(self):
        key = base64.b64encode(b"0123456789abcdef").decode()
        uri = f"ss://{b64('2022-blake3-aes-128-gcm:' + key + ':' + key)}@1.2.3.4:443#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["method"], "2022-blake3-aes-128-gcm")

    def test_obfs_plugin_rejected(self):
        creds = b64("aes-128-gcm:secret")
        uri = f"ss://{creds}@1.2.3.4:443?plugin=obfs-local%3Bobfs%3Dhttp#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "ss-plugin-obfs")

    def test_unknown_method_rejected(self):
        uri = "ss://" + b64("chacha20-poly1305:secret@1.2.3.4:443") + "#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "ss-method-chacha20-poly1305")


class TrojanTests(unittest.TestCase):
    def test_tls_is_forced(self):
        uri = (
            "trojan://humanity@172.66.40.99:443"
            "?allowInsecure=0&sni=www.trusteeforward.com&type=ws&path=/assignment#x"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "trojan")
        self.assertEqual(out["password"], "humanity")
        self.assertTrue(out["tls"]["enabled"])
        self.assertEqual(out["tls"]["server_name"], "www.trusteeforward.com")
        self.assertEqual(out["transport"]["type"], "ws")

    def test_percent_encoded_password(self):
        uri = "trojan://Trojan%4082164024@18.168.148.212:443?security=tls&sni=gb.tronsg.com#x"
        out, _ = uris.parse_uri(uri, "p1")
        self.assertEqual(out["password"], "Trojan@82164024")


class Hysteria2Tests(unittest.TestCase):
    def test_salamander_obfs(self):
        uri = (
            "hysteria2://77f73bd5-51bf-4143-8ebd-02f56ba376f4@177.1.195.242:24000"
            "?insecure=0&sni=hy.kirian.su&obfs=salamander&obfs-password=9VK3Nqd0bcX#x"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "hysteria2")
        self.assertEqual(out["obfs"], {"type": "salamander", "password": "9VK3Nqd0bcX"})
        self.assertNotIn("insecure", out["tls"])

    def test_obfs_without_password(self):
        uri = "hysteria2://pass@1.2.3.4:24000?obfs=salamander&sni=a.b#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "hy2-obfs-without-password")

    def test_missing_port(self):
        uri = "hysteria2://bce6c821-200d-421f-bf3d-7159e5246ea0@hy2.123266.xyz:33333/?sni=hy2.123266.xyz#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["server_port"], 33333)


class SocksAndHttpTests(unittest.TestCase):
    def test_socks5_with_auth(self):
        out, reason = uris.parse_uri("socks5://user:pass@1.2.3.4:1080#x", "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "socks")
        self.assertEqual(out["version"], "5")
        self.assertEqual(out["username"], "user")
        self.assertEqual(out["password"], "pass")

    def test_socks5_without_auth(self):
        out, _ = uris.parse_uri("socks5://45.74.31.42:5654#x", "p1")
        self.assertNotIn("username", out)

    def test_plain_http(self):
        out, _ = uris.parse_uri("http://170.238.38.15:8080#x", "p1")
        self.assertEqual(out["type"], "http")
        self.assertEqual(out["server_port"], 8080)
        self.assertNotIn("tls", out)

    def test_https_with_placeholder_credentials(self):
        out, reason = uris.parse_uri("https://:None@crosscards.site:443#x", "p1")
        self.assertIsNone(reason)
        self.assertTrue(out["tls"]["enabled"])
        self.assertEqual(out["tls"]["server_name"], "crosscards.site")
        self.assertNotIn("username", out)


class TuicTests(unittest.TestCase):
    def test_basic(self):
        uri = "tuic://e75ad2eb-6c1f-45ce-8023-f5f10875df66:secret@1.2.3.4:443?sni=a.b#x"
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason)
        self.assertEqual(out["type"], "tuic")
        self.assertEqual(out["uuid"], "e75ad2eb-6c1f-45ce-8023-f5f10875df66")
        self.assertEqual(out["password"], "secret")
        self.assertEqual(out["tls"]["alpn"], ["h3"])

    def test_without_password(self):
        out, reason = uris.parse_uri("tuic://uuid@1.2.3.4:443#x", "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "tuic-without-password")


class HelpersTests(unittest.TestCase):
    def test_dedupe_key_ignores_display_name(self):
        a = "vless://u@1.2.3.4:443?security=tls#%5BOpenRay%5D%20US-1"
        b = "vless://u@1.2.3.4:443?security=tls#another%20name"
        self.assertEqual(uris.dedupe_key(a), uris.dedupe_key(b))

    def test_uri_name_and_endpoint(self):
        uri = "vless://u@1.2.3.4:8443?security=tls#%F0%9F%87%BA%F0%9F%87%B8US-1"
        self.assertEqual(uris.uri_name(uri), "🇺🇸US-1")
        self.assertEqual(uris.uri_endpoint(uri), ("1.2.3.4", 8443))

    def test_endpoint_for_vmess_and_ss(self):
        uri = vmess({"add": "5.6.7.8", "port": "443", "id": "u", "net": "tcp"})
        self.assertEqual(uris.uri_endpoint(uri), ("5.6.7.8", 443))
        uri = "ss://" + b64("aes-128-gcm:secret@9.9.9.9:4000") + "#x"
        self.assertEqual(uris.uri_endpoint(uri), ("9.9.9.9", 4000))

    def test_unknown_scheme(self):
        out, reason = uris.parse_uri("wireguard://u@1.2.3.4:443#x", "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "scheme-wireguard")

    def test_looks_like_hostname(self):
        self.assertTrue(uris.looks_like_hostname("x.m-90.xyz"))
        self.assertTrue(uris.looks_like_hostname("185.104.63.173"))
        self.assertFalse(uris.looks_like_hostname("/?TELEGRAM--i10VPN"))
        self.assertFalse(uris.looks_like_hostname("/"))
        self.assertFalse(uris.looks_like_hostname(""))
        self.assertFalse(uris.looks_like_hostname("a b"))


class GoldenLinesTests(unittest.TestCase):
    """Exact lines taken from githubmirror/{1,6,22,23,24,25}.txt."""

    def check(self, uri, expected_type, expected_server, expected_port):
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(reason, f"{uri[:60]} -> {reason}")
        self.assertEqual(out["type"], expected_type)
        self.assertEqual(out["server"], expected_server)
        self.assertEqual(out["server_port"], expected_port)
        return out

    def test_reality_vless(self):
        uri = (
            "vless://e75ad2eb-6c1f-45ce-8023-f5f10875df66@185.104.63.173:443/"
            "?type=tcp&encryption=none&flow=xtls-rprx-vision&sni=zsat.eu-cdn294.com"
            "&fp=firefox&security=reality"
            "&pbk=Dj1TD7Sy_TciG915ffXFpMu_pYHnrpGo_ypyyDw44Uc&sid=8fbdc8d37cc76852"
            "#%5BOpenRay%5D%20%F0%9F%87%A6%F0%9F%87%B9AT-1"
        )
        out = self.check(uri, "vless", "185.104.63.173", 443)
        self.assertEqual(out["tls"]["server_name"], "zsat.eu-cdn294.com")
        self.assertEqual(out["tls"]["utls"]["fingerprint"], "firefox")
        self.assertEqual(out["flow"], "xtls-rprx-vision")

    def test_grpc_vless(self):
        uri = (
            "vless://2f35965a-9a9b-45fd-ba32-987296dfb6be@rs2.univesalsrv.com:443"
            "?mode=gun&security=reality&encryption=none"
            "&pbk=tL16MVY08r-7YDXb1_gxuBBWInpSFp97ZLJ_ax3R2iE&fp=chrome&type=grpc"
            "&serviceName=media.v1.ObjectService&sni=rs2.univesalsrv.com&sid=1469af2040b7c323"
            "#%5BOpenRay%5D"
        )
        out = self.check(uri, "vless", "rs2.univesalsrv.com", 443)
        self.assertEqual(out["transport"], {"type": "grpc", "service_name": "media.v1.ObjectService"})

    def test_socks5(self):
        uri = "socks5://45.74.31.42:5654#%5BOpenRay%5D%20%F0%9F%87%BA%F0%9F%87%B8US-2"
        self.check(uri, "socks", "45.74.31.42", 5654)

    def test_http_proxy(self):
        uri = "http://170.238.38.15:8080#%5BOpenRay%5D%20%F0%9F%87%A7%F0%9F%87%B7BR-2"
        self.check(uri, "http", "170.238.38.15", 8080)

    def test_cloudflare_worker_vless(self):
        uri = (
            "vless://ea29d6f1-3567-4d45-b8c2-e42f162caef4@mute-dawn-f27b.375.workers.dev:8880"
            "?type=ws&path=%2Fpyip%3DProxyIP.JP.CMLiussss.net"
            "&sni=mute-dawn-f27b.375.workers.dev#%5BOpenRay%5D%20%F0%9F%8C%90XX-6"
        )
        out = self.check(uri, "vless", "mute-dawn-f27b.375.workers.dev", 8880)
        self.assertEqual(out["transport"]["type"], "ws")

    def test_xhttp_line_is_rejected(self):
        uri = (
            "vless://b804593e-8b69-5cd0-9082-5ca59f59eeec@173.199.71.90:443"
            "?encryption=none&fp=&mode=auto&path=%2F48bf90eba6bb"
            "&pbk=ctzP6t-rVczgXwSI0p9iJaiOxCxCeAr7dic2q9n08kU&security=reality"
            "&sid=2d217da6b57e3d9d&sni=www.vimeo.com&type=xhttp#x"
        )
        out, reason = uris.parse_uri(uri, "p1")
        self.assertIsNone(out)
        self.assertEqual(reason, "transport-xhttp-unsupported")


if __name__ == "__main__":
    unittest.main(verbosity=2)
