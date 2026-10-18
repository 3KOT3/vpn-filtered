# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T04:45:43Z** UTC (прогон занял 40 с)

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
| YouTube доступен | 99 |
| + Telegram (HTTP) доступен | 93 |
| + дата-центр Telegram доступен | 93 |
| + скорость ≥ 3.0 Мбит/с | 52 |
| **В итоговом списке** | **52** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 46 |
| vmess | 3 |
| shadowsocks | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| PH | 7 |
| DE | 5 |
| FI | 5 |
| PL | 5 |
| JP | 4 |
| US | 3 |
| NL | 3 |
| TR | 2 |
| SG | 2 |
| IN | 2 |
| BR | 2 |
| CA | 1 |
| AT | 1 |
| IT | 1 |
| ?? | 1 |
| LT | 1 |
| SE | 1 |
| HK | 1 |
| RU | 1 |
| MD | 1 |
| KR | 1 |
| ID | 1 |
| KH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 58.50 | 36 | 343 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 29.18 | 54 | 307 |
| 3 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 17.22 | 198 | 241 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.50 | 186 | 720 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 16.40 | 199 | 221 |
| 6 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 14.91 | 261 | 276 |
| 7 | 🇮🇹[openproxylist.com] vless-IT | vless | IT | 14.64 | 212 | 282 |
| 8 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.34 | 340 | 626 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 13.80 | 197 | 205 |
| 10 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 13.56 | 250 | 314 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
