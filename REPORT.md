# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-10T13:59:32Z** UTC (прогон занял 44 с)

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
| Разобрано в конфиги | 406 |
| Уникальных | 406 |
| Endpoint отвечает по TCP | 391 |
| YouTube доступен | 190 |
| + Telegram (HTTP) доступен | 178 |
| + дата-центр Telegram доступен | 178 |
| + скорость ≥ 3.0 Мбит/с | 95 |
| **В итоговом списке** | **95** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 50 |
| shadowsocks | 32 |
| vless | 12 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 50 |
| IT | 11 |
| CA | 9 |
| ?? | 6 |
| DE | 3 |
| SE | 3 |
| CH | 3 |
| ES | 2 |
| LT | 2 |
| MX | 1 |
| FR | 1 |
| AT | 1 |
| GB | 1 |
| EE | 1 |
| NL | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 12.39 | 50 | 279 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.14 | 69 | 339 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.01 | 77 | 341 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.87 | 74 | 406 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.31 | 83 | 441 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.13 | 73 | 387 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.86 | 137 | 412 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.45 | 74 | 388 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.02 | 75 | 369 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.89 | 77 | 424 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 33 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
