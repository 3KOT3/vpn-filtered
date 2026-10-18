# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:40:04Z** UTC (прогон занял 34 с)

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
| Endpoint отвечает по TCP | 105 |
| YouTube доступен | 68 |
| + Telegram (HTTP) доступен | 59 |
| + дата-центр Telegram доступен | 59 |
| + скорость ≥ 3.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 33 |
| shadowsocks | 2 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 11 |
| PL | 4 |
| DE | 4 |
| US | 2 |
| HK | 2 |
| JP | 2 |
| IT | 1 |
| CZ | 1 |
| LV | 1 |
| LT | 1 |
| SE | 1 |
| BY | 1 |
| FI | 1 |
| BR | 1 |
| PH | 1 |
| KH | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 29.48 | 37 | 346 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 13.91 | 58 | 326 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 10.58 | 194 | 227 |
| 4 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.12 | 239 | 272 |
| 5 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.73 | 257 | 290 |
| 6 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 9.52 | 232 | 269 |
| 7 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 9.35 | 219 | 306 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 9.32 | 235 | 338 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 9.20 | 221 | 323 |
| 10 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 9.08 | 274 | 525 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
