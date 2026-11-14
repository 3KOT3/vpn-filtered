# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-14T12:44:32Z** UTC (прогон занял 42 с)

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
| Строк в источниках | 447 |
| Разобрано в конфиги | 442 |
| Уникальных | 442 |
| Endpoint отвечает по TCP | 415 |
| YouTube доступен | 149 |
| + Telegram (HTTP) доступен | 140 |
| + дата-центр Telegram доступен | 140 |
| + скорость ≥ 3.0 Мбит/с | 71 |
| **В итоговом списке** | **71** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 39 |
| vmess | 25 |
| vless | 7 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 45 |
| CA | 10 |
| DE | 3 |
| GB | 2 |
| FR | 2 |
| IT | 2 |
| ?? | 1 |
| CH | 1 |
| ES | 1 |
| TW | 1 |
| KR | 1 |
| NL | 1 |
| SE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.61 | 37 | 510 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.03 | 68 | 527 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.92 | 74 | 475 |
| 4 | [🇺🇸] [vm-no-ra] [261114-051933.796] | vmess | US | 12.92 | 72 | 479 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.53 | 65 | 437 |
| 6 | [🇺🇸] [vm-no-ra] [261114-051933.758] | vmess | US | 12.19 | 72 | 473 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.26 | 73 | 417 |
| 8 | 🇺🇸[openproxylist.com] vless-US | vless | US | 10.94 | 41 | 493 |
| 9 | [🇺🇸] [vm-no-ra] [261114-051933.719] | vmess | US | 10.77 | 70 | 476 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.67 | 34 | 455 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
