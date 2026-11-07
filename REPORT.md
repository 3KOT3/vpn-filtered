# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-07T21:15:09Z** UTC (прогон занял 42 с)

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
| Строк в источниках | 418 |
| Разобрано в конфиги | 395 |
| Уникальных | 395 |
| Endpoint отвечает по TCP | 386 |
| YouTube доступен | 260 |
| + Telegram (HTTP) доступен | 207 |
| + дата-центр Telegram доступен | 207 |
| + скорость ≥ 3.0 Мбит/с | 104 |
| **В итоговом списке** | **104** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 59 |
| vmess | 26 |
| vless | 16 |
| trojan | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 52 |
| DE | 14 |
| CA | 8 |
| ES | 7 |
| FR | 6 |
| ?? | 4 |
| NL | 4 |
| CH | 4 |
| GB | 2 |
| JP | 1 |
| PL | 1 |
| AT | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 17.84 | 28 | 478 |
| 2 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.92 | 56 | 480 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.16 | 54 | 504 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.04 | 55 | 477 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.01 | 34 | 441 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 10.99 | 64 | 411 |
| 7 | [🇺🇸] [vm-no-ra] [261107-213137.618] | vmess | US | 10.76 | 102 | 673 |
| 8 | 🇺🇸[openproxylist.com] vless-US | vless | US | 10.34 | 57 | 526 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.23 | 71 | 399 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.11 | 97 | 419 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 16 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
