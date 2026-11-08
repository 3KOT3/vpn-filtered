# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-08T12:30:23Z** UTC (прогон занял 77 с)

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
| Разобрано в конфиги | 437 |
| Уникальных | 437 |
| Endpoint отвечает по TCP | 418 |
| YouTube доступен | 195 |
| + Telegram (HTTP) доступен | 176 |
| + дата-центр Telegram доступен | 176 |
| + скорость ≥ 3.0 Мбит/с | 111 |
| **В итоговом списке** | **111** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 54 |
| vmess | 47 |
| vless | 10 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 56 |
| DE | 15 |
| CA | 14 |
| ?? | 4 |
| FR | 4 |
| ES | 4 |
| CH | 4 |
| IT | 4 |
| GB | 3 |
| SE | 2 |
| AT | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 23.24 | 59 | 358 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 22.06 | 68 | 345 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.46 | 36 | 371 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 15.91 | 72 | 351 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 15.17 | 46 | 350 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.80 | 71 | 369 |
| 7 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 12.34 | 117 | 659 |
| 8 | [🇨🇦] [vm-no-ra] [261108-101318.939] | vmess | CA | 12.26 | 77 | 320 |
| 9 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 11.84 | 85 | 336 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.70 | 73 | 370 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 6 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
