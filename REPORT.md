# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T16:21:58Z** UTC (прогон занял 28 с)

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
| Разобрано в конфиги | 18 |
| Уникальных | 18 |
| Endpoint отвечает по TCP | 18 |
| YouTube доступен | 17 |
| + Telegram (HTTP) доступен | 17 |
| + дата-центр Telegram доступен | 17 |
| + скорость ≥ 3.0 Мбит/с | 15 |
| **В итоговом списке** | **15** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 11 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 7 |
| JP | 3 |
| AT | 1 |
| CZ | 1 |
| IT | 1 |
| SE | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.89 | 233 | 963 |
| 2 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.71 | 232 | 967 |
| 3 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 8.62 | 306 | 348 |
| 4 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 8.07 | 350 | 371 |
| 5 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 7.99 | 445 | 943 |
| 6 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 7.91 | 340 | 384 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 7.79 | 382 | 1142 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 7.78 | 338 | 360 |
| 9 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.23 | 319 | 1113 |
| 10 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 6.95 | 445 | 463 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 124 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
