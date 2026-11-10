# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-10T00:59:57Z** UTC (прогон занял 52 с)

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
| Строк в источниках | 448 |
| Разобрано в конфиги | 366 |
| Уникальных | 366 |
| Endpoint отвечает по TCP | 344 |
| YouTube доступен | 238 |
| + Telegram (HTTP) доступен | 221 |
| + дата-центр Telegram доступен | 221 |
| + скорость ≥ 3.0 Мбит/с | 107 |
| **В итоговом списке** | **107** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 55 |
| vmess | 38 |
| vless | 13 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 55 |
| IT | 12 |
| CA | 8 |
| DE | 7 |
| NL | 7 |
| ?? | 4 |
| GB | 4 |
| ES | 3 |
| FR | 2 |
| CH | 1 |
| SE | 1 |
| EE | 1 |
| AT | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.26 | 44 | 372 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.72 | 70 | 396 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.55 | 69 | 362 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.43 | 81 | 545 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.31 | 94 | 376 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.97 | 84 | 385 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.83 | 83 | 388 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.74 | 87 | 401 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.56 | 84 | 390 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.06 | 84 | 489 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 72 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
