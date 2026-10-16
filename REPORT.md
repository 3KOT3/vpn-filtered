# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T01:52:35Z** UTC (прогон занял 67 с)

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
| Разобрано в конфиги | 133 |
| Уникальных | 133 |
| Endpoint отвечает по TCP | 129 |
| YouTube доступен | 105 |
| + Telegram (HTTP) доступен | 102 |
| + дата-центр Telegram доступен | 102 |
| + скорость ≥ 2.0 Мбит/с | 64 |
| **В итоговом списке** | **64** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 45 |
| trojan | 11 |
| vmess | 5 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 8 |
| SG | 6 |
| KR | 6 |
| PL | 5 |
| NL | 5 |
| DE | 5 |
| US | 4 |
| SE | 3 |
| FI | 3 |
| CA | 2 |
| JP | 2 |
| TR | 2 |
| HK | 2 |
| GB | 1 |
| UA | 1 |
| KH | 1 |
| AT | 1 |
| IT | 1 |
| ES | 1 |
| LT | 1 |
| ID | 1 |
| TH | 1 |
| IN | 1 |
| CH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 20.14 | 101 | 588 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.84 | 134 | 370 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.61 | 151 | 384 |
| 4 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 16.88 | 496 | 438 |
| 5 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 14.20 | 166 | 422 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.13 | 259 | 562 |
| 7 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 11.10 | 365 | 440 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 10.57 | 281 | 283 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 10.42 | 279 | 292 |
| 10 | 🇬🇧[openproxylist.com] vless-GB | vless | GB | 10.29 | 1104 | 511 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
