# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:03:35Z** UTC (прогон занял 43 с)

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
| YouTube доступен | 76 |
| + Telegram (HTTP) доступен | 64 |
| + дата-центр Telegram доступен | 64 |
| + скорость ≥ 3.0 Мбит/с | 30 |
| **В итоговом списке** | **30** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 25 |
| shadowsocks | 2 |
| vmess | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 16 |
| JP | 2 |
| PL | 2 |
| FI | 2 |
| US | 1 |
| BR | 1 |
| LT | 1 |
| DE | 1 |
| TR | 1 |
| HU | 1 |
| EE | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 31.64 | 75 | 519 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 16.33 | 209 | 426 |
| 3 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 10.22 | 228 | 973 |
| 4 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.95 | 317 | 1067 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 9.82 | 230 | 989 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.79 | 333 | 379 |
| 7 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.46 | 355 | 421 |
| 8 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.46 | 371 | 388 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 9.26 | 336 | 424 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.26 | 341 | 406 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
