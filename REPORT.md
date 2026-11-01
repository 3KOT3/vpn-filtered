# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-01T12:21:54Z** UTC (прогон занял 41 с)

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
| Строк в источниках | 440 |
| Разобрано в конфиги | 419 |
| Уникальных | 419 |
| Endpoint отвечает по TCP | 413 |
| YouTube доступен | 289 |
| + Telegram (HTTP) доступен | 267 |
| + дата-центр Telegram доступен | 267 |
| + скорость ≥ 3.0 Мбит/с | 71 |
| **В итоговом списке** | **71** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 28 |
| vless | 24 |
| vmess | 19 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 39 |
| CA | 15 |
| AR | 5 |
| GB | 4 |
| DE | 2 |
| MX | 1 |
| CL | 1 |
| NL | 1 |
| KR | 1 |
| PL | 1 |
| ES | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 27.47 | 46 | 694 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 23.95 | 32 | 457 |
| 3 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 23.44 | 43 | 644 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 23.17 | 16 | 426 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 22.55 | 18 | 406 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 22.36 | 18 | 407 |
| 7 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 21.84 | 16 | 408 |
| 8 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 21.59 | 39 | 677 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 21.34 | 44 | 726 |
| 10 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 21.12 | 43 | 633 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 6 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
