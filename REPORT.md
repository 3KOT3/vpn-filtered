# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-08T03:29:36Z** UTC (прогон занял 37 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 512 КБ за не более 15 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 442 |
| Разобрано в конфиги | 420 |
| Уникальных | 420 |
| Endpoint отвечает по TCP | 417 |
| YouTube доступен | 280 |
| + Telegram (HTTP) доступен | 270 |
| + дата-центр Telegram доступен | 270 |
| + скорость ≥ 3.0 Мбит/с | 179 |
| **В итоговом списке** | **179** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 67 |
| vless | 67 |
| vmess | 43 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 122 |
| DE | 14 |
| CA | 9 |
| FR | 7 |
| ES | 6 |
| GB | 4 |
| CH | 4 |
| SE | 4 |
| ?? | 3 |
| NL | 3 |
| SG | 1 |
| FI | 1 |
| IT | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 36.23 | 35 | 323 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 34.36 | 25 | 321 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 30.53 | 44 | 317 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.10 | 53 | 390 |
| 5 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 14.69 | 48 | 310 |
| 6 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 14.42 | 116 | 324 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.97 | 367 | 272 |
| 8 | 🇨🇦[openproxylist.com] ss-CA | shadowsocks | CA | 13.36 | 103 | 298 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.16 | 71 | 385 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.79 | 73 | 362 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 16 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
