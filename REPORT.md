# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:50:59Z** UTC (прогон занял 48 с)

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
| Endpoint отвечает по TCP | 115 |
| YouTube доступен | 72 |
| + Telegram (HTTP) доступен | 63 |
| + дата-центр Telegram доступен | 63 |
| + скорость ≥ 3.0 Мбит/с | 31 |
| **В итоговом списке** | **31** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 27 |
| shadowsocks | 3 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 17 |
| FI | 3 |
| PL | 2 |
| US | 1 |
| NL | 1 |
| DE | 1 |
| LT | 1 |
| HU | 1 |
| TR | 1 |
| BR | 1 |
| JP | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.70 | 187 | 635 |
| 2 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.71 | 190 | 202 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 13.56 | 205 | 341 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 13.30 | 211 | 288 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 12.91 | 223 | 337 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.82 | 226 | 274 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.72 | 227 | 262 |
| 8 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.98 | 255 | 286 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 11.95 | 238 | 303 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 11.65 | 216 | 267 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
