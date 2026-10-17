# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:24:50Z** UTC (прогон занял 50 с)

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
| Endpoint отвечает по TCP | 117 |
| YouTube доступен | 79 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 3.0 Мбит/с | 30 |
| **В итоговом списке** | **30** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 26 |
| shadowsocks | 3 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 15 |
| FI | 3 |
| JP | 3 |
| PL | 2 |
| US | 1 |
| HU | 1 |
| LT | 1 |
| TR | 1 |
| EE | 1 |
| BR | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 31.30 | 67 | 333 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.03 | 192 | 632 |
| 3 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 14.33 | 217 | 238 |
| 4 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 14.30 | 230 | 266 |
| 5 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 13.66 | 230 | 271 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 13.45 | 266 | 267 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 12.85 | 232 | 304 |
| 8 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 12.07 | 256 | 336 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 11.78 | 236 | 308 |
| 10 | 🇭🇺[openproxylist.com] vless-HU | vless | HU | 11.72 | 275 | 290 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
