# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:23:16Z** UTC (прогон занял 39 с)

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
| Endpoint отвечает по TCP | 114 |
| YouTube доступен | 70 |
| + Telegram (HTTP) доступен | 58 |
| + дата-центр Telegram доступен | 58 |
| + скорость ≥ 3.0 Мбит/с | 30 |
| **В итоговом списке** | **30** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 23 |
| shadowsocks | 4 |
| vmess | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| PL | 2 |
| JP | 2 |
| US | 1 |
| FI | 1 |
| LT | 1 |
| EE | 1 |
| TR | 1 |
| BR | 1 |
| TW | 1 |
| RU | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 22.97 | 82 | 380 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 22.66 | 152 | 627 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 12.28 | 323 | 298 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.89 | 267 | 323 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 11.70 | 298 | 352 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 11.69 | 270 | 326 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.41 | 309 | 346 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.87 | 276 | 340 |
| 9 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 10.61 | 298 | 370 |
| 10 | 🇱🇹[openproxylist.com] vless-LT | vless | LT | 10.56 | 354 | 397 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
