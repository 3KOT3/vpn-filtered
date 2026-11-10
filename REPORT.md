# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-10T22:40:29Z** UTC (прогон занял 42 с)

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
| Строк в источниках | 447 |
| Разобрано в конфиги | 381 |
| Уникальных | 381 |
| Endpoint отвечает по TCP | 375 |
| YouTube доступен | 238 |
| + Telegram (HTTP) доступен | 229 |
| + дата-центр Telegram доступен | 229 |
| + скорость ≥ 3.0 Мбит/с | 128 |
| **В итоговом списке** | **128** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 57 |
| shadowsocks | 44 |
| vless | 26 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 66 |
| CA | 19 |
| IT | 14 |
| DE | 6 |
| NL | 6 |
| FR | 4 |
| CH | 3 |
| SE | 2 |
| ES | 2 |
| MX | 1 |
| GB | 1 |
| LT | 1 |
| BG | 1 |
| BE | 1 |
| EE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 23.31 | 45 | 275 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 19.10 | 37 | 351 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 17.65 | 36 | 357 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 15.58 | 44 | 350 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 15.43 | 76 | 373 |
| 6 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 14.85 | 52 | 403 |
| 7 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 14.69 | 47 | 434 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.50 | 71 | 346 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.38 | 76 | 390 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.23 | 115 | 402 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 62 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
