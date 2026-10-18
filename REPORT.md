# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T13:53:35Z** UTC (прогон занял 41 с)

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
| Разобрано в конфиги | 140 |
| Уникальных | 140 |
| Endpoint отвечает по TCP | 123 |
| YouTube доступен | 75 |
| + Telegram (HTTP) доступен | 61 |
| + дата-центр Telegram доступен | 61 |
| + скорость ≥ 3.0 Мбит/с | 33 |
| **В итоговом списке** | **33** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| shadowsocks | 3 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 17 |
| JP | 4 |
| US | 2 |
| FI | 2 |
| PL | 2 |
| AT | 1 |
| DE | 1 |
| IT | 1 |
| BY | 1 |
| KR | 1 |
| CZ | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 24.97 | 97 | 674 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.07 | 88 | 397 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 12.54 | 163 | 418 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 8.77 | 237 | 842 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 8.15 | 231 | 984 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.03 | 232 | 978 |
| 7 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 7.72 | 332 | 408 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 7.51 | 354 | 392 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 7.38 | 352 | 405 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 7.19 | 308 | 344 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
