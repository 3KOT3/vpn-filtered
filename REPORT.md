# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-01T03:23:05Z** UTC (прогон занял 34 с)

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
| Строк в источниках | 441 |
| Разобрано в конфиги | 410 |
| Уникальных | 410 |
| Endpoint отвечает по TCP | 403 |
| YouTube доступен | 267 |
| + Telegram (HTTP) доступен | 253 |
| + дата-центр Telegram доступен | 253 |
| + скорость ≥ 3.0 Мбит/с | 139 |
| **В итоговом списке** | **139** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 83 |
| trojan | 35 |
| vmess | 21 |

## По странам

| Страна | В списке |
| --- | ---: |
| CA | 42 |
| US | 40 |
| DE | 13 |
| GB | 11 |
| ES | 9 |
| NL | 8 |
| PL | 3 |
| CZ | 2 |
| FR | 2 |
| EE | 2 |
| SE | 2 |
| MX | 1 |
| CH | 1 |
| FI | 1 |
| LV | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 20.22 | 35 | 281 |
| 2 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 19.11 | 53 | 270 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 17.70 | 53 | 345 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 17.18 | 59 | 334 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 16.05 | 55 | 265 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 14.15 | 66 | 346 |
| 7 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 13.32 | 72 | 383 |
| 8 | 🇨🇦[openproxylist.com] trojan-CA | trojan | CA | 13.12 | 64 | 314 |
| 9 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.32 | 72 | 361 |
| 10 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.13 | 72 | 396 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 10 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
