# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T16:12:50Z** UTC (прогон занял 55 с)

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
| Endpoint отвечает по TCP | 117 |
| YouTube доступен | 62 |
| + Telegram (HTTP) доступен | 53 |
| + дата-центр Telegram доступен | 53 |
| + скорость ≥ 3.0 Мбит/с | 37 |
| **В итоговом списке** | **37** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 30 |
| shadowsocks | 4 |
| vmess | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 20 |
| JP | 3 |
| US | 2 |
| IT | 1 |
| AT | 1 |
| FI | 1 |
| PL | 1 |
| CZ | 1 |
| HK | 1 |
| GB | 1 |
| KR | 1 |
| SE | 1 |
| BY | 1 |
| EE | 1 |
| LV | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 18.79 | 72 | 553 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.86 | 120 | 415 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 10.66 | 159 | 442 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 8.42 | 222 | 599 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.39 | 228 | 967 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.01 | 235 | 978 |
| 7 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.02 | 312 | 1061 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 6.89 | 320 | 332 |
| 9 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 6.70 | 329 | 364 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 6.61 | 349 | 387 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
