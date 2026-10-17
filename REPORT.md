# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T16:55:26Z** UTC (прогон занял 42 с)

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
| Строк в источниках | 147 |
| Разобрано в конфиги | 111 |
| Уникальных | 111 |
| Endpoint отвечает по TCP | 106 |
| YouTube доступен | 79 |
| + Telegram (HTTP) доступен | 70 |
| + дата-центр Telegram доступен | 70 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 32 |
| vmess | 4 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| PL | 4 |
| FI | 3 |
| US | 2 |
| DE | 2 |
| JP | 2 |
| EE | 1 |
| HU | 1 |
| TR | 1 |
| BR | 1 |
| NL | 1 |
| KR | 1 |
| IN | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 29.39 | 40 | 343 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.82 | 199 | 631 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 15.81 | 54 | 752 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 15.70 | 247 | 305 |
| 5 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 14.26 | 238 | 324 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.19 | 237 | 341 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.90 | 337 | 759 |
| 8 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.89 | 224 | 319 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 12.60 | 235 | 324 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.43 | 229 | 273 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
