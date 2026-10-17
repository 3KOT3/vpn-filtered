# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:41:28Z** UTC (прогон занял 40 с)

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
| YouTube доступен | 78 |
| + Telegram (HTTP) доступен | 67 |
| + дата-центр Telegram доступен | 67 |
| + скорость ≥ 3.0 Мбит/с | 31 |
| **В итоговом списке** | **31** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 26 |
| shadowsocks | 2 |
| vmess | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| FI | 3 |
| JP | 2 |
| PL | 2 |
| US | 1 |
| BR | 1 |
| NL | 1 |
| EE | 1 |
| TR | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 34.91 | 61 | 630 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 15.38 | 169 | 449 |
| 3 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 12.26 | 236 | 1024 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 11.80 | 226 | 954 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 10.28 | 355 | 1051 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 10.05 | 332 | 344 |
| 7 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.35 | 343 | 394 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 9.13 | 381 | 481 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 8.85 | 528 | 661 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 8.78 | 349 | 418 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
