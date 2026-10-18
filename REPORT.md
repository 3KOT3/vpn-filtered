# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:14:40Z** UTC (прогон занял 43 с)

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
| Endpoint отвечает по TCP | 103 |
| YouTube доступен | 67 |
| + Telegram (HTTP) доступен | 54 |
| + дата-центр Telegram доступен | 54 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 33 |
| vmess | 4 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 11 |
| PL | 4 |
| DE | 4 |
| JP | 3 |
| KR | 3 |
| US | 2 |
| HK | 2 |
| BR | 1 |
| FR | 1 |
| IT | 1 |
| CZ | 1 |
| LT | 1 |
| BY | 1 |
| FI | 1 |
| LV | 1 |
| SG | 1 |
| PH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.41 | 129 | 419 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.80 | 292 | 605 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 12.38 | 153 | 445 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 9.65 | 232 | 941 |
| 5 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 9.35 | 212 | 950 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.02 | 213 | 947 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 7.42 | 319 | 340 |
| 8 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 7.41 | 315 | 376 |
| 9 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 7.24 | 345 | 378 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 7.06 | 345 | 428 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
