# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T10:14:55Z** UTC (прогон занял 64 с)

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
| Разобрано в конфиги | 121 |
| Уникальных | 121 |
| Endpoint отвечает по TCP | 114 |
| YouTube доступен | 78 |
| + Telegram (HTTP) доступен | 63 |
| + дата-центр Telegram доступен | 63 |
| + скорость ≥ 2.0 Мбит/с | 38 |
| **В итоговом списке** | **38** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| trojan | 6 |
| vmess | 2 |
| shadowsocks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 14 |
| US | 4 |
| BR | 3 |
| DE | 2 |
| PL | 2 |
| FI | 2 |
| IN | 2 |
| KR | 2 |
| CA | 1 |
| KH | 1 |
| HK | 1 |
| TR | 1 |
| ID | 1 |
| JP | 1 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 37.56 | 46 | 626 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 27.64 | 69 | 291 |
| 3 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 27.56 | 68 | 349 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 25.94 | 146 | 454 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.26 | 167 | 659 |
| 6 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.57 | 270 | 297 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 12.67 | 371 | 377 |
| 8 | 🇰🇭[openproxylist.com] vless-KH | vless | KH | 12.21 | 252 | 238 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 11.48 | 292 | 388 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 10.94 | 264 | 353 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
