# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-14T10:45:09Z** UTC (прогон занял 119 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 131 |
| Уникальных | 131 |
| Endpoint отвечает по TCP | 126 |
| YouTube доступен | 71 |
| + Telegram (HTTP) доступен | 61 |
| + дата-центр Telegram доступен | 61 |
| + скорость ≥ 2.0 Мбит/с | 25 |
| **В итоговом списке** | **25** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 15 |
| trojan | 6 |
| vmess | 2 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 5 |
| SG | 5 |
| DE | 4 |
| US | 2 |
| PL | 2 |
| FI | 2 |
| AT | 1 |
| NL | 1 |
| HK | 1 |
| EE | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 32.17 | 112 | 365 |
| 2 |  | vmess | ?? | 28.12 | 101 | 540 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 23.39 | 125 | 622 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 12.49 | 257 | 255 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.23 | 247 | 275 |
| 6 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 11.29 | 333 | 375 |
| 7 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.81 | 291 | 359 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.20 | 327 | 304 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 9.69 | 385 | 486 |
| 10 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 8.98 | 443 | 538 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
