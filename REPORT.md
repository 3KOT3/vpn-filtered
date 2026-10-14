# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-14T16:03:09Z** UTC (прогон занял 72 с)

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
| Строк в источниках | 149 |
| Разобрано в конфиги | 142 |
| Уникальных | 142 |
| Endpoint отвечает по TCP | 136 |
| YouTube доступен | 84 |
| + Telegram (HTTP) доступен | 72 |
| + дата-центр Telegram доступен | 72 |
| + скорость ≥ 2.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 21 |
| trojan | 10 |
| shadowsocks | 3 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 10 |
| US | 5 |
| NL | 4 |
| SG | 4 |
| FI | 2 |
| KR | 2 |
| DE | 1 |
| AT | 1 |
| IT | 1 |
| GB | 1 |
| SE | 1 |
| PL | 1 |
| HK | 1 |
| ID | 1 |
| JP | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 30.75 | 124 | 1243 |
| 2 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 16.70 | 200 | 209 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.42 | 209 | 686 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 15.31 | 209 | 224 |
| 5 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.76 | 294 | 298 |
| 6 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 13.61 | 235 | 276 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.47 | 42 | 307 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 13.33 | 252 | 1371 |
| 9 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 12.90 | 239 | 332 |
| 10 | 🇬🇧[openproxylist.com] vless-GB | vless | GB | 12.21 | 159 | 4293 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
