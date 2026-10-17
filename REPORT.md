# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T15:48:33Z** UTC (прогон занял 43 с)

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
| YouTube доступен | 82 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 3.0 Мбит/с | 27 |
| **В итоговом списке** | **27** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 23 |
| shadowsocks | 3 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 15 |
| FI | 3 |
| NL | 2 |
| PL | 2 |
| US | 1 |
| LT | 1 |
| JP | 1 |
| DE | 1 |
| TR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.95 | 141 | 688 |
| 2 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 10.62 | 227 | 229 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 9.69 | 298 | 354 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 9.53 | 288 | 362 |
| 5 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.35 | 284 | 320 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 9.29 | 281 | 295 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.29 | 308 | 340 |
| 8 | 🇱🇹[openproxylist.com] vless-LT | vless | LT | 9.13 | 351 | 401 |
| 9 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 8.84 | 308 | 452 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.82 | 307 | 371 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
