# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-15T03:54:32Z** UTC (прогон занял 38 с)

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
| Строк в источниках | 446 |
| Разобрано в конфиги | 438 |
| Уникальных | 438 |
| Endpoint отвечает по TCP | 432 |
| YouTube доступен | 282 |
| + Telegram (HTTP) доступен | 268 |
| + дата-центр Telegram доступен | 268 |
| + скорость ≥ 3.0 Мбит/с | 166 |
| **В итоговом списке** | **166** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 78 |
| vmess | 56 |
| shadowsocks | 32 |

## По странам

| Страна | В списке |
| --- | ---: |
| CA | 70 |
| US | 50 |
| ?? | 11 |
| IT | 11 |
| DE | 4 |
| SE | 4 |
| GB | 3 |
| FR | 3 |
| CH | 3 |
| ES | 2 |
| BY | 2 |
| EE | 1 |
| AT | 1 |
| BE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 16.90 | 48 | 347 |
| 2 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 16.60 | 58 | 412 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 16.13 | 49 | 370 |
| 4 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 15.91 | 49 | 369 |
| 5 | 🇨🇦[openproxylist.com] ss-CA | shadowsocks | CA | 13.13 | 91 | 473 |
| 6 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 12.56 | 83 | 373 |
| 7 | 🏳[openproxylist.com] vmess- | vmess | ?? | 12.18 | 75 | 352 |
| 8 | 🇨🇦[openproxylist.com] vmess-CA | vmess | CA | 10.50 | 118 | 324 |
| 9 | 🇺🇸[openproxylist.com] vless-US | vless | US | 10.39 | 117 | 404 |
| 10 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 10.37 | 109 | 379 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 6 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
