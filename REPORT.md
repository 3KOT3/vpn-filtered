# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:54:06Z** UTC (прогон занял 40 с)

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
| Разобрано в конфиги | 140 |
| Уникальных | 140 |
| Endpoint отвечает по TCP | 120 |
| YouTube доступен | 63 |
| + Telegram (HTTP) доступен | 54 |
| + дата-центр Telegram доступен | 54 |
| + скорость ≥ 3.0 Мбит/с | 28 |
| **В итоговом списке** | **28** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 24 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 14 |
| JP | 3 |
| US | 2 |
| SE | 2 |
| FI | 2 |
| IT | 1 |
| AT | 1 |
| PL | 1 |
| CZ | 1 |
| BY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 19.47 | 58 | 581 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.46 | 133 | 427 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.96 | 246 | 647 |
| 4 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.60 | 218 | 957 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 9.29 | 212 | 954 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 7.14 | 340 | 348 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 6.95 | 308 | 359 |
| 8 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 6.74 | 346 | 379 |
| 9 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.72 | 308 | 1054 |
| 10 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 6.60 | 348 | 403 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
