# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-20T14:38:55Z** UTC (прогон занял 44 с)

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
| Строк в источниках | 444 |
| Разобрано в конфиги | 412 |
| Уникальных | 412 |
| Endpoint отвечает по TCP | 393 |
| YouTube доступен | 159 |
| + Telegram (HTTP) доступен | 135 |
| + дата-центр Telegram доступен | 135 |
| + скорость ≥ 3.0 Мбит/с | 69 |
| **В итоговом списке** | **69** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 33 |
| vmess | 29 |
| vless | 7 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 34 |
| CA | 8 |
| ?? | 8 |
| FR | 6 |
| GB | 3 |
| DE | 2 |
| IT | 2 |
| NL | 1 |
| ES | 1 |
| SE | 1 |
| CH | 1 |
| AT | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.70 | 87 | 400 |
| 2 | [🇺🇸] [vm-no-ra] [261120-061441.229] | vmess | US | 11.14 | 94 | 373 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.88 | 109 | 565 |
| 4 | 🇨🇦[openproxylist.com] ss-CA | shadowsocks | CA | 10.80 | 106 | 526 |
| 5 | [🇨🇦] [vm-no-ra] [261120-061542.203] | vmess | CA | 10.67 | 97 | 339 |
| 6 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 10.37 | 119 | 361 |
| 7 | [🇺🇸] [vl-re-ra] [261120-061018.740] | vless | US | 9.98 | 73 | 333 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.93 | 108 | 533 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.91 | 191 | 414 |
| 10 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 9.90 | 86 | 352 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 24 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
