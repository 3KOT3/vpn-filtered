# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:31:30Z** UTC (прогон занял 48 с)

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
| Endpoint отвечает по TCP | 116 |
| YouTube доступен | 80 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 3.0 Мбит/с | 32 |
| **В итоговом списке** | **32** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 25 |
| shadowsocks | 3 |
| vmess | 3 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| JP | 2 |
| PL | 2 |
| FI | 2 |
| US | 1 |
| BR | 1 |
| HU | 1 |
| EE | 1 |
| LT | 1 |
| DE | 1 |
| TR | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 30.27 | 69 | 566 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 17.24 | 160 | 423 |
| 3 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 12.38 | 234 | 975 |
| 4 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 11.52 | 245 | 984 |
| 5 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 10.16 | 319 | 1052 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.70 | 330 | 379 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.17 | 398 | 406 |
| 8 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.01 | 343 | 383 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 8.91 | 371 | 429 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 8.91 | 781 | 532 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
