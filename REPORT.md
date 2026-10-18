# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T04:37:44Z** UTC (прогон занял 39 с)

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
| Строк в источниках | 149 |
| Разобрано в конфиги | 130 |
| Уникальных | 130 |
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 94 |
| + Telegram (HTTP) доступен | 81 |
| + дата-центр Telegram доступен | 81 |
| + скорость ≥ 3.0 Мбит/с | 48 |
| **В итоговом списке** | **48** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 36 |
| vmess | 5 |
| trojan | 4 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 6 |
| SG | 5 |
| PL | 5 |
| JP | 5 |
| DE | 4 |
| FI | 4 |
| ?? | 3 |
| NL | 2 |
| TR | 2 |
| CA | 1 |
| AT | 1 |
| IT | 1 |
| HK | 1 |
| LT | 1 |
| BR | 1 |
| KR | 1 |
| EE | 1 |
| RU | 1 |
| ID | 1 |
| MD | 1 |
| TW | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 32.10 | 72 | 373 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 27.99 | 86 | 370 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 26.02 | 102 | 555 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 21.43 | 138 | 589 |
| 5 | 🇸🇬[openproxylist.com] vless-SG | vless | SG | 17.69 | 471 | 945 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.65 | 304 | 590 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.59 | 99 | 320 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.09 | 258 | 261 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 13.01 | 249 | 291 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.01 | 274 | 352 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
