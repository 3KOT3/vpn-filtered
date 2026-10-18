# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:58:04Z** UTC (прогон занял 49 с)

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
| Endpoint отвечает по TCP | 120 |
| YouTube доступен | 67 |
| + Telegram (HTTP) доступен | 56 |
| + дата-центр Telegram доступен | 56 |
| + скорость ≥ 3.0 Мбит/с | 33 |
| **В итоговом списке** | **33** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 18 |
| JP | 3 |
| US | 2 |
| PL | 2 |
| IT | 1 |
| AT | 1 |
| FI | 1 |
| LV | 1 |
| CZ | 1 |
| EE | 1 |
| SE | 1 |
| BY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 18.59 | 102 | 595 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.06 | 91 | 381 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 11.47 | 168 | 405 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.40 | 240 | 600 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.61 | 239 | 980 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.38 | 231 | 968 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 7.88 | 304 | 360 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 7.54 | 330 | 300 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 7.04 | 310 | 321 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 6.90 | 332 | 373 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
