#!/usr/bin/env bash
# Установка серверной проверки на Ubuntu/Debian (VPS в России, мини-ПК, Raspberry Pi).
#
#   sudo CHECKER_KEY='...' WORKER_URL='https://moybot.<аккаунт>.workers.dev' bash install.sh
#
# Ставит Python и sing-box, раскладывает службу, создаёт systemd-юнит и запускает.
set -euo pipefail

CHECKER_KEY="${CHECKER_KEY:-}"
WORKER_URL="${WORKER_URL:-}"
INTERVAL_HOURS="${INTERVAL_HOURS:-6}"
MIN_MBPS="${MIN_MBPS:-2.0}"
SOURCES="${SOURCES:-}"
PORT="${PORT:-8099}"
APP_DIR="${APP_DIR:-/opt/vpn-checker}"
SING_BOX_VERSION="${SING_BOX_VERSION:-1.14.3}"

if [ -z "$CHECKER_KEY" ]; then
  echo "Нужен CHECKER_KEY — придумайте длинный пароль и передайте его так:"
  echo "  sudo CHECKER_KEY='мой-пароль' WORKER_URL='https://...' bash install.sh"
  exit 1
fi
if [ -z "$WORKER_URL" ]; then
  echo "Нужен WORKER_URL — адрес воркера бота, например https://moybot.xxx.workers.dev"
  exit 1
fi
if [ "$(id -u)" != "0" ]; then
  echo "Запускать от root: sudo ... bash install.sh"
  exit 1
fi

echo "==> пакеты"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq python3 curl tar ca-certificates >/dev/null

ARCH="$(uname -m)"
case "$ARCH" in
  x86_64) SB_ARCH="amd64" ;;
  aarch64|arm64) SB_ARCH="arm64" ;;
  armv7l) SB_ARCH="armv7" ;;
  *) echo "неизвестная архитектура: $ARCH"; exit 1 ;;
esac

echo "==> sing-box $SING_BOX_VERSION ($SB_ARCH)"
mkdir -p "$APP_DIR/bin"
if [ ! -x "$APP_DIR/bin/sing-box" ]; then
  TMP="$(mktemp -d)"
  curl -fsSL -o "$TMP/sb.tar.gz" \
    "https://github.com/SagerNet/sing-box/releases/download/v${SING_BOX_VERSION}/sing-box-${SING_BOX_VERSION}-linux-${SB_ARCH}.tar.gz"
  tar -xzf "$TMP/sb.tar.gz" -C "$TMP"
  cp "$TMP"/sing-box-*/sing-box "$APP_DIR/bin/sing-box"
  chmod +x "$APP_DIR/bin/sing-box"
  rm -rf "$TMP"
fi
"$APP_DIR/bin/sing-box" version | head -2

echo "==> файлы службы"
mkdir -p "$APP_DIR/checker"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
cp "$SCRIPT_DIR/server.py" "$APP_DIR/server.py"
cp "$REPO_ROOT/checker/check.py" "$APP_DIR/checker/check.py"
cp "$REPO_ROOT/checker/uris.py" "$APP_DIR/checker/uris.py"
cp "$REPO_ROOT/checker/config.json" "$APP_DIR/checker/config.json"

echo "==> systemd"
cat >/etc/systemd/system/vpn-checker.service <<UNIT
[Unit]
Description=VPN config checker (server side)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=$APP_DIR
Environment=CHECKER_KEY=$CHECKER_KEY
Environment=WORKER_URL=$WORKER_URL
Environment=INTERVAL_HOURS=$INTERVAL_HOURS
Environment=MIN_MBPS=$MIN_MBPS
Environment=SOURCES=$SOURCES
Environment=PORT=$PORT
Environment=REPO_ROOT=$APP_DIR
Environment=SING_BOX=$APP_DIR/bin/sing-box
ExecStart=/usr/bin/python3 $APP_DIR/server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
UNIT

systemctl daemon-reload
systemctl enable vpn-checker >/dev/null
systemctl restart vpn-checker
sleep 3

echo
echo "==> проверка"
curl -fsS "http://127.0.0.1:${PORT}/health" || {
  echo "служба не отвечает, смотрите: journalctl -u vpn-checker -n 50 --no-pager"
  exit 1
}

echo
echo "Готово. Служба работает и сама проверяет конфиги каждые ${INTERVAL_HOURS} ч."
echo "Первую проверку можно запустить вручную из бота кнопкой «🔄 Обновить»."
echo "Логи: journalctl -u vpn-checker -f"
