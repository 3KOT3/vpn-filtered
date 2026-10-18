# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:24:00Z** UTC (прогон занял 27 с)

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
| YouTube доступен | 64 |
| + Telegram (HTTP) доступен | 54 |
| + дата-центр Telegram доступен | 54 |
| + скорость ≥ 3.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 30 |
| vmess | 4 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 11 |
| PL | 4 |
| JP | 3 |
| DE | 3 |
| US | 2 |
| HK | 2 |
| BR | 1 |
| IT | 1 |
| FR | 1 |
| LT | 1 |
| BY | 1 |
| SE | 1 |
| FI | 1 |
| CZ | 1 |
| MY | 1 |
| KR | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.38 | 93 | 386 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.96 | 238 | 892 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 12.67 | 170 | 438 |
| 4 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 9.05 | 231 | 983 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.79 | 231 | 1000 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 8.65 | 234 | 965 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 7.79 | 311 | 321 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 7.68 | 331 | 408 |
| 9 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 7.24 | 334 | 377 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 7.04 | 344 | 416 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
