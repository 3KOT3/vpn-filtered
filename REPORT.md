# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:20:27Z** UTC (прогон занял 36 с)

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
| YouTube доступен | 72 |
| + Telegram (HTTP) доступен | 62 |
| + дата-центр Telegram доступен | 62 |
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
| ?? | 17 |
| PL | 3 |
| FI | 3 |
| JP | 2 |
| US | 1 |
| HU | 1 |
| LT | 1 |
| DE | 1 |
| BR | 1 |
| IN | 1 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 26.08 | 106 | 387 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 23.41 | 135 | 590 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 12.64 | 273 | 377 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.40 | 333 | 340 |
| 5 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.12 | 269 | 330 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.09 | 257 | 307 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 11.68 | 264 | 364 |
| 8 | 🇭🇺[openproxylist.com] vless-HU | vless | HU | 11.50 | 327 | 341 |
| 9 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.47 | 302 | 326 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 11.39 | 268 | 340 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
