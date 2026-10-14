# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-14T21:03:06Z** UTC (прогон занял 75 с)

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
| Строк в источниках | 147 |
| Разобрано в конфиги | 135 |
| Уникальных | 135 |
| Endpoint отвечает по TCP | 129 |
| YouTube доступен | 94 |
| + Telegram (HTTP) доступен | 85 |
| + дата-центр Telegram доступен | 85 |
| + скорость ≥ 2.0 Мбит/с | 49 |
| **В итоговом списке** | **49** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 36 |
| trojan | 6 |
| vmess | 5 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 6 |
| DE | 5 |
| US | 4 |
| FI | 4 |
| SG | 4 |
| NL | 3 |
| PL | 3 |
| HK | 3 |
| SE | 3 |
| EE | 2 |
| TR | 2 |
| KR | 2 |
| IT | 1 |
| IE | 1 |
| ES | 1 |
| GB | 1 |
| TH | 1 |
| JP | 1 |
| AT | 1 |
| AE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 33.60 | 93 | 371 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 27.51 | 134 | 365 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 23.47 | 134 | 667 |
| 4 |  | vmess | ?? | 18.32 | 156 | 605 |
| 5 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.08 | 234 | 298 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.32 | 272 | 327 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.85 | 262 | 271 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.33 | 251 | 279 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 11.64 | 264 | 367 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 11.41 | 298 | 357 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
