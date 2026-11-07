# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-07T12:09:08Z** UTC (прогон занял 59 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 512 КБ за не более 15 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 445 |
| Разобрано в конфиги | 438 |
| Уникальных | 438 |
| Endpoint отвечает по TCP | 426 |
| YouTube доступен | 194 |
| + Telegram (HTTP) доступен | 177 |
| + дата-центр Telegram доступен | 177 |
| + скорость ≥ 3.0 Мбит/с | 116 |
| **В итоговом списке** | **116** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 69 |
| vmess | 29 |
| vless | 16 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 55 |
| DE | 13 |
| CA | 12 |
| FR | 6 |
| ?? | 5 |
| ES | 5 |
| GB | 5 |
| CH | 5 |
| NL | 4 |
| SE | 3 |
| IT | 1 |
| PL | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 19.35 | 75 | 349 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 17.34 | 37 | 405 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.16 | 71 | 367 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.60 | 49 | 356 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.31 | 72 | 366 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.05 | 70 | 365 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.93 | 115 | 315 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.68 | 100 | 438 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 8.54 | 68 | 361 |
| 10 | [🇺🇸] [vm-no-ra] [261107-044634.310] | vmess | US | 8.44 | 150 | 469 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 3 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
