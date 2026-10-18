# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:41:13Z** UTC (прогон занял 39 с)

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
| Endpoint отвечает по TCP | 101 |
| YouTube доступен | 60 |
| + Telegram (HTTP) доступен | 56 |
| + дата-центр Telegram доступен | 56 |
| + скорость ≥ 3.0 Мбит/с | 37 |
| **В итоговом списке** | **37** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 32 |
| vmess | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 12 |
| PL | 4 |
| DE | 3 |
| US | 2 |
| HK | 2 |
| JP | 2 |
| FR | 1 |
| IT | 1 |
| CZ | 1 |
| LV | 1 |
| LT | 1 |
| FI | 1 |
| BY | 1 |
| NL | 1 |
| BR | 1 |
| SE | 1 |
| KR | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 25.34 | 35 | 334 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 21.09 | 51 | 313 |
| 3 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 11.85 | 189 | 231 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 10.32 | 195 | 223 |
| 5 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.96 | 270 | 279 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.74 | 232 | 269 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.58 | 339 | 572 |
| 8 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 9.46 | 218 | 322 |
| 9 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 9.34 | 232 | 275 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 9.34 | 234 | 325 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
