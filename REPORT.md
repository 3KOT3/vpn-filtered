# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T16:17:09Z** UTC (прогон занял 24 с)

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
| Endpoint отвечает по TCP | 16 |
| YouTube доступен | 13 |
| + Telegram (HTTP) доступен | 13 |
| + дата-центр Telegram доступен | 13 |
| + скорость ≥ 3.0 Мбит/с | 9 |
| **В итоговом списке** | **9** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 6 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 4 |
| JP | 3 |
| IT | 1 |
| CZ | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.70 | 234 | 969 |
| 2 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.29 | 234 | 981 |
| 3 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 8.89 | 313 | 428 |
| 4 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 7.88 | 333 | 377 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.72 | 322 | 1109 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 7.10 | 329 | 1061 |
| 7 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 6.94 | 453 | 826 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 6.69 | 346 | 436 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 5.88 | 572 | 630 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 124 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
