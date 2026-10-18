# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:15:03Z** UTC (прогон занял 46 с)

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
| Endpoint отвечает по TCP | 124 |
| YouTube доступен | 70 |
| + Telegram (HTTP) доступен | 61 |
| + дата-центр Telegram доступен | 61 |
| + скорость ≥ 3.0 Мбит/с | 35 |
| **В итоговом списке** | **35** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| shadowsocks | 4 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| JP | 4 |
| US | 2 |
| DE | 2 |
| GB | 1 |
| AT | 1 |
| IT | 1 |
| FI | 1 |
| PL | 1 |
| BY | 1 |
| KR | 1 |
| CZ | 1 |
| EE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 12.21 | 100 | 547 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.03 | 90 | 414 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 8.48 | 165 | 435 |
| 4 | 🇬🇧[openproxylist.com] vless-GB | vless | GB | 7.39 | 261 | 310 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.05 | 235 | 964 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.82 | 233 | 964 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 6.77 | 242 | 635 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 6.71 | 345 | 315 |
| 9 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 6.35 | 302 | 345 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 6.17 | 308 | 331 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
