# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T06:32:50Z** UTC (прогон занял 58 с)

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
| Строк в источниках | 660 |
| Разобрано в конфиги | 633 |
| Уникальных | 633 |
| Endpoint отвечает по TCP | 617 |
| YouTube доступен | 322 |
| + Telegram (HTTP) доступен | 289 |
| + дата-центр Telegram доступен | 289 |
| + скорость ≥ 3.0 Мбит/с | 187 |
| **В итоговом списке** | **187** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 138 |
| vmess | 44 |
| shadowsocks | 4 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 36 |
| CA | 23 |
| DE | 23 |
| PL | 21 |
| SG | 12 |
| PH | 10 |
| JP | 9 |
| NL | 8 |
| GB | 7 |
| LT | 6 |
| FI | 5 |
| HK | 3 |
| EE | 3 |
| FR | 3 |
| CZ | 2 |
| IT | 2 |
| ?? | 2 |
| PA | 2 |
| AT | 1 |
| TR | 1 |
| SE | 1 |
| MD | 1 |
| ID | 1 |
| IN | 1 |
| LV | 1 |
| ES | 1 |
| AE | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 25.86 | 83 | 436 |
| 2 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 12.81 | 64 | 582 |
| 3 | [🇨🇦] [vm-no-ra] [261018-025900.206] | vmess | CA | 12.04 | 114 | 359 |
| 4 | 🇺🇸 United States, Phoenix | [BL] | vless | US | 11.90 | 111 | 370 |
| 5 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 11.34 | 340 | 470 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.02 | 280 | 604 |
| 7 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 10.81 | 296 | 638 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.80 | 330 | 359 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.16 | 293 | 311 |
| 10 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 10.14 | 327 | 358 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 14 |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
