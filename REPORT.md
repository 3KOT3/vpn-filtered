# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:42:18Z** UTC (прогон занял 44 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 120 |
| Уникальных | 120 |
| Endpoint отвечает по TCP | 104 |
| YouTube доступен | 66 |
| + Telegram (HTTP) доступен | 61 |
| + дата-центр Telegram доступен | 61 |
| + скорость ≥ 3.0 Мбит/с | 38 |
| **В итоговом списке** | **38** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 33 |
| vmess | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 13 |
| JP | 4 |
| PL | 4 |
| DE | 3 |
| US | 2 |
| HK | 2 |
| KR | 2 |
| BR | 1 |
| FR | 1 |
| IT | 1 |
| CZ | 1 |
| BY | 1 |
| SE | 1 |
| FI | 1 |
| PH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.02 | 120 | 429 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.09 | 203 | 425 |
| 3 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 9.06 | 229 | 1004 |
| 4 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.91 | 227 | 961 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 8.58 | 225 | 979 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.95 | 511 | 908 |
| 7 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 7.61 | 309 | 372 |
| 8 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 7.40 | 360 | 425 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 7.14 | 324 | 350 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 7.08 | 359 | 425 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
