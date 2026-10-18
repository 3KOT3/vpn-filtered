# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:59:16Z** UTC (прогон занял 40 с)

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
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 69 |
| + Telegram (HTTP) доступен | 63 |
| + дата-центр Telegram доступен | 63 |
| + скорость ≥ 3.0 Мбит/с | 38 |
| **В итоговом списке** | **38** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 34 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 22 |
| JP | 3 |
| FI | 2 |
| PL | 2 |
| US | 1 |
| IT | 1 |
| AT | 1 |
| SE | 1 |
| BY | 1 |
| GB | 1 |
| CZ | 1 |
| LV | 1 |
| EE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 20.49 | 59 | 336 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.34 | 36 | 325 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 11.48 | 188 | 682 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.86 | 211 | 294 |
| 5 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 9.26 | 225 | 276 |
| 6 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 9.01 | 241 | 323 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 8.98 | 204 | 226 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 8.94 | 266 | 292 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 8.44 | 230 | 290 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 8.44 | 236 | 306 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
