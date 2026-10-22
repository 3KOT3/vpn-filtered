# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-22T21:00:29Z** UTC (прогон занял 62 с)

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
| Строк в источниках | 349 |
| Разобрано в конфиги | 314 |
| Уникальных | 314 |
| Endpoint отвечает по TCP | 296 |
| YouTube доступен | 180 |
| + Telegram (HTTP) доступен | 154 |
| + дата-центр Telegram доступен | 154 |
| + скорость ≥ 3.0 Мбит/с | 41 |
| **В итоговом списке** | **41** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 16 |
| vmess | 14 |
| shadowsocks | 8 |
| trojan | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 13 |
| CA | 13 |
| GB | 4 |
| ES | 3 |
| ?? | 2 |
| NL | 1 |
| IT | 1 |
| AT | 1 |
| DE | 1 |
| PL | 1 |
| SE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 8.68 | 31 | 283 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 8.34 | 24 | 286 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 7.15 | 36 | 339 |
| 4 | [🇺🇸] [vl-re-ra] [261022-210607.556] | vless | US | 7.08 | 38 | 267 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 6.63 | 39 | 742 |
| 6 | [🇨🇦] [vm-no-ra] [261022-211150.430] | vmess | CA | 5.45 | 297 | 315 |
| 7 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 5.30 | 46 | 415 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 5.21 | 59 | 319 |
| 9 | [🇨🇦] [vm-no-ra] [261022-211150.276] | vmess | CA | 5.08 | 102 | 312 |
| 10 | [🇺🇸] [vm-no-ra] [261022-211128.288] | vmess | US | 4.87 | 28 | 267 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 11 |
| vmess-http-obfs | 4 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
