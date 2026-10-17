# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T14:59:19Z** UTC (прогон занял 44 с)

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
| Endpoint отвечает по TCP | 117 |
| YouTube доступен | 74 |
| + Telegram (HTTP) доступен | 68 |
| + дата-центр Telegram доступен | 68 |
| + скорость ≥ 3.0 Мбит/с | 29 |
| **В итоговом списке** | **29** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 26 |
| shadowsocks | 2 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 16 |
| PL | 2 |
| FI | 2 |
| NL | 2 |
| US | 1 |
| HU | 1 |
| LT | 1 |
| DE | 1 |
| TR | 1 |
| BR | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 31.19 | 60 | 310 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.71 | 188 | 673 |
| 3 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.13 | 234 | 273 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 13.07 | 234 | 306 |
| 5 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 13.06 | 259 | 306 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 12.96 | 238 | 248 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.92 | 211 | 264 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.70 | 229 | 281 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 12.56 | 208 | 271 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 12.38 | 220 | 333 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
