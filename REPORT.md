# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:20:42Z** UTC (прогон занял 35 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 120 |
| Уникальных | 120 |
| Endpoint отвечает по TCP | 103 |
| YouTube доступен | 60 |
| + Telegram (HTTP) доступен | 54 |
| + дата-центр Telegram доступен | 54 |
| + скорость ≥ 3.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 32 |
| shadowsocks | 2 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 12 |
| PL | 4 |
| DE | 4 |
| US | 3 |
| HK | 2 |
| JP | 2 |
| IT | 1 |
| CZ | 1 |
| SE | 1 |
| LT | 1 |
| NL | 1 |
| BY | 1 |
| FI | 1 |
| BR | 1 |
| PH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 31.05 | 37 | 331 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 22.04 | 51 | 355 |
| 3 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.35 | 236 | 301 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 9.81 | 194 | 212 |
| 5 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 9.34 | 261 | 277 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.26 | 340 | 655 |
| 7 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 9.10 | 265 | 561 |
| 8 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 8.98 | 220 | 310 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 8.93 | 220 | 325 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.65 | 274 | 283 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
