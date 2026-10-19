#!/usr/bin/env bash
# Проверка VPN-конфигов на российском сервере (Cloud.ru Evolution free tier, любой VPS).
#
#   sudo CHECKER_KEY='chk-...' bash install.sh
#
# Ставит Python и sing-box, кладёт проект в /opt/vpn-checker, включает таймер
# systemd: каждые N часов проверка идёт из России и публикует список боту.
set -euo pipefail

CHECKER_KEY="${CHECKER_KEY:-}"
PUBLISH_KEY="${PUBLISH_KEY:-pub-7Qm2xVp9LzR4tNb8sWk3}"
WORKER_URL="${WORKER_URL:-https://moybot.sergeylllilllkin2.workers.dev}"
MIN_MBPS="${MIN_MBPS:-1.0}"
SOURCES="${SOURCES:-6,22,23}"
INTERVAL_HOURS="${INTERVAL_HOURS:-2}"
SING_BOX_VERSION="${SING_BOX_VERSION:-1.14.3}"
APP_DIR="${APP_DIR:-/opt/vpn-checker}"
REPO_URL="${REPO_URL:-https://github.com/3KOT3/vpn-filtered.git}"

if [ -z "$CHECKER_KEY" ]; then
  echo "Нужен CHECKER_KEY — секрет, которым бот принимает список:"
  echo "  sudo CHECKER_KEY='chk-7Qm2xVp9LzR4tNb8sWk3' bash install.sh"
  exit 1
fi
if [ "$(id -u)" != "0" ]; then
  echo "Запускать от root: sudo ... bash install.sh"
  exit 1
fi

echo "==> пакеты"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq python3 curl git tar ca-certificates >/dev/null

echo "==> код"
if [ -d "$APP_DIR/.git" ]; then
  git -C "$APP_DIR" pull --ff-only -q || true
else
  rm -rf "$APP_DIR"
  git clone --depth 1 "$REPO_URL" "$APP_DIR"
fi

echo "==> sing-box $SING_BOX_VERSION"
mkdir -p "$APP_DIR/bin"
if [ ! -x "$APP_DIR/bin/sing-box" ]; then
  TMP="$(mktemp -d)"
  case "$(uname -m)" in
    x86_64) SB_ARCH="amd64" ;;
    aarch64|arm64) SB_ARCH="arm64" ;;
    *) echo "неизвестная архитектура: $(uname -m)"; exit 1 ;;
  esac
  curl -fsSL --retry 3 -o "$TMP/sb.tar.gz" \
    "https://github.com/SagerNet/sing-box/releases/download/v${SING_BOX_VERSION}/sing-box-${SING_BOX_VERSION}-linux-${SB_ARCH}.tar.gz"
  tar -xzf "$TMP/sb.tar.gz" -C "$TMP"
  cp "$TMP"/sing-box-*/sing-box "$APP_DIR/bin/sing-box"
  chmod +x "$APP_DIR/bin/sing-box"
  rm -rf "$TMP"
fi
"$APP_DIR/bin/sing-box" version | head -2

echo "==> скрипт проверки"
cat >"$APP_DIR/run.sh" <<RUN
#!/usr/bin/env bash
set -u
cd "$APP_DIR"
mkdir -p "$APP_DIR/out" "$APP_DIR/work" "$APP_DIR/src"
/usr/bin/python3 "$APP_DIR/checker/check.py" \
  --sing-box "$APP_DIR/bin/sing-box" \
  --out-dir "$APP_DIR/out" \
  --work-dir "$APP_DIR/work" \
  --cache-dir "$APP_DIR/src" \
  --min-mbps "$MIN_MBPS" \
  --min-keep 1 \
  --source-files "$SOURCES"
rc=\$?
echo "check.py rc=\$rc"
/usr/bin/python3 "$APP_DIR/deploy/vm/publish.py"
exit 0
RUN
chmod +x "$APP_DIR/run.sh"

echo "==> systemd"
cat >/etc/systemd/system/vpn-checker.service <<UNIT
[Unit]
Description=VPN config checker (Russia)
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=$APP_DIR
Environment=WORKER_URL=$WORKER_URL
Environment=CHECKER_KEY=$CHECKER_KEY
Environment=PUBLISH_KEY=$PUBLISH_KEY
ExecStart=$APP_DIR/run.sh
TimeoutStartSec=900
UNIT

cat >/etc/systemd/system/vpn-checker.timer <<TIMER
[Unit]
Description=Run VPN config checker every ${INTERVAL_HOURS}h

[Timer]
OnBootSec=2min
OnUnitActiveSec=${INTERVAL_HOURS}h
AccuracySec=1min
Unit=vpn-checker.service

[Install]
WantedBy=timers.target
TIMER

systemctl daemon-reload
systemctl enable --now vpn-checker.timer >/dev/null

echo "==> первый прогон (2–3 минуты)"
systemctl start vpn-checker.service || true
sleep 5
journalctl -u vpn-checker.service -n 20 --no-pager || true

echo
echo "Готово. Проверка идёт из России и повторяется каждые ${INTERVAL_HOURS} ч."
echo "Таймер:  systemctl list-timers vpn-checker.timer"
echo "Логи:    journalctl -u vpn-checker.service -f"
