# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:00:29Z** UTC (прогон занял 52 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 145 |
| Разобрано в конфиги | 129 |
| Уникальных | 129 |
| Endpoint отвечает по TCP | 116 |
| YouTube доступен | 81 |
| + Telegram (HTTP) доступен | 65 |
| + дата-центр Telegram доступен | 65 |
| + скорость ≥ 3.0 Мбит/с | 32 |
| **В итоговом списке** | **32** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 16 |
| JP | 3 |
| FI | 3 |
| PL | 2 |
| US | 1 |
| HU | 1 |
| LT | 1 |
| DE | 1 |
| TW | 1 |
| TR | 1 |
| NL | 1 |
| BR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 31.18 | 74 | 625 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 15.94 | 158 | 432 |
| 3 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.60 | 333 | 380 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.22 | 395 | 389 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.12 | 313 | 1067 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.10 | 342 | 382 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 8.73 | 395 | 850 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 8.62 | 357 | 421 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.59 | 358 | 400 |
| 10 | 🇭🇺[openproxylist.com] vless-HU | vless | HU | 8.56 | 389 | 407 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
