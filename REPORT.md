# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-08T21:29:52Z** UTC (прогон занял 48 с)

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
| Строк в источниках | 432 |
| Разобрано в конфиги | 392 |
| Уникальных | 392 |
| Endpoint отвечает по TCP | 381 |
| YouTube доступен | 273 |
| + Telegram (HTTP) доступен | 248 |
| + дата-центр Telegram доступен | 248 |
| + скорость ≥ 3.0 Мбит/с | 124 |
| **В итоговом списке** | **124** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 65 |
| vmess | 47 |
| vless | 11 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 67 |
| CA | 13 |
| DE | 12 |
| FR | 6 |
| GB | 5 |
| ?? | 4 |
| CH | 4 |
| SE | 4 |
| ES | 3 |
| NL | 2 |
| IT | 2 |
| AT | 1 |
| IL | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.07 | 72 | 360 |
| 2 | [🇨🇦] [vm-no-ra] [261108-195436.250] | vmess | CA | 13.50 | 90 | 376 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.13 | 73 | 366 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.07 | 72 | 382 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.79 | 107 | 325 |
| 6 | [🇨🇦] [vm-no-ra] [261108-195436.343] | vmess | CA | 12.77 | 86 | 374 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.75 | 68 | 359 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.50 | 77 | 339 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.44 | 74 | 362 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.24 | 73 | 385 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 31 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
