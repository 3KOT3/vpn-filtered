# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:41:30Z** UTC (прогон занял 44 с)

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
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 74 |
| + Telegram (HTTP) доступен | 64 |
| + дата-центр Telegram доступен | 64 |
| + скорость ≥ 3.0 Мбит/с | 37 |
| **В итоговом списке** | **37** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 31 |
| shadowsocks | 4 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| JP | 4 |
| US | 2 |
| PL | 2 |
| FI | 2 |
| DE | 2 |
| EE | 2 |
| AT | 1 |
| IT | 1 |
| BY | 1 |
| SE | 1 |
| CZ | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.09 | 67 | 383 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 9.29 | 137 | 642 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 6.31 | 283 | 288 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 6.24 | 279 | 340 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 6.19 | 311 | 393 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 6.18 | 303 | 358 |
| 7 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 6.13 | 292 | 313 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 6.00 | 282 | 380 |
| 9 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 5.94 | 281 | 1051 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 5.93 | 268 | 334 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
