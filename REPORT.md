# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T10:13:08Z** UTC (прогон занял 29 с)

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
| Разобрано в конфиги | 120 |
| Уникальных | 120 |
| Endpoint отвечает по TCP | 101 |
| YouTube доступен | 63 |
| + Telegram (HTTP) доступен | 55 |
| + дата-центр Telegram доступен | 55 |
| + скорость ≥ 3.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 30 |
| vmess | 4 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 8 |
| JP | 4 |
| PL | 3 |
| DE | 3 |
| US | 2 |
| SE | 2 |
| HK | 2 |
| KR | 2 |
| FR | 1 |
| IT | 1 |
| CZ | 1 |
| BR | 1 |
| BY | 1 |
| NL | 1 |
| IN | 1 |
| SG | 1 |
| FI | 1 |
| PH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 23.75 | 70 | 370 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 15.16 | 86 | 333 |
| 3 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 10.51 | 229 | 284 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 9.65 | 275 | 266 |
| 5 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 8.74 | 259 | 338 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.70 | 275 | 835 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 8.55 | 266 | 366 |
| 8 | 🇺🇸[openproxylist.com] vless-US | vless | US | 8.45 | 303 | 618 |
| 9 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 8.24 | 273 | 344 |
| 10 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 8.24 | 464 | 683 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
