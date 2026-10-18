# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T16:29:17Z** UTC (прогон занял 14 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 15 |
| Уникальных | 15 |
| Endpoint отвечает по TCP | 15 |
| YouTube доступен | 15 |
| + Telegram (HTTP) доступен | 15 |
| + дата-центр Telegram доступен | 15 |
| + скорость ≥ 2.0 Мбит/с | 13 |
| **В итоговом списке** | **13** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 10 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 7 |
| JP | 2 |
| AT | 1 |
| IT | 1 |
| FI | 1 |
| SE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.29 | 229 | 269 |
| 2 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 11.21 | 252 | 278 |
| 3 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 10.67 | 238 | 276 |
| 4 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 9.42 | 343 | 371 |
| 5 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 9.14 | 373 | 354 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 8.11 | 388 | 736 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 8.01 | 251 | 330 |
| 8 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.10 | 338 | 1075 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 6.59 | 328 | 1066 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 5.99 | 639 | 925 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 127 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
