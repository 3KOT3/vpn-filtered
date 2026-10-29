# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-29T03:35:28Z** UTC (прогон занял 47 с)

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
| Строк в источниках | 439 |
| Разобрано в конфиги | 418 |
| Уникальных | 418 |
| Endpoint отвечает по TCP | 415 |
| YouTube доступен | 292 |
| + Telegram (HTTP) доступен | 276 |
| + дата-центр Telegram доступен | 276 |
| + скорость ≥ 3.0 Мбит/с | 111 |
| **В итоговом списке** | **111** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 67 |
| vmess | 23 |
| trojan | 17 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| CA | 37 |
| US | 34 |
| GB | 12 |
| NL | 6 |
| FR | 3 |
| FI | 3 |
| CH | 3 |
| RU | 3 |
| IT | 2 |
| BY | 2 |
| ES | 2 |
| CZ | 1 |
| SE | 1 |
| EE | 1 |
| CL | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 14.25 | 56 | 261 |
| 2 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 13.16 | 57 | 332 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.31 | 85 | 495 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.24 | 56 | 335 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.47 | 72 | 387 |
| 6 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 11.43 | 48 | 489 |
| 7 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 11.24 | 37 | 505 |
| 8 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 10.86 | 52 | 300 |
| 9 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 10.71 | 43 | 406 |
| 10 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 10.65 | 42 | 408 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 12 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
