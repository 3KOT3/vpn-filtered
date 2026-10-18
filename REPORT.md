# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T06:24:35Z** UTC (прогон занял 47 с)

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
| Строк в источниках | 147 |
| Разобрано в конфиги | 141 |
| Уникальных | 141 |
| Endpoint отвечает по TCP | 136 |
| YouTube доступен | 99 |
| + Telegram (HTTP) доступен | 87 |
| + дата-центр Telegram доступен | 87 |
| + скорость ≥ 3.0 Мбит/с | 44 |
| **В итоговом списке** | **44** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 37 |
| shadowsocks | 4 |
| vmess | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| PH | 7 |
| DE | 6 |
| JP | 5 |
| US | 4 |
| NL | 3 |
| HK | 3 |
| FI | 3 |
| PL | 2 |
| AT | 1 |
| IT | 1 |
| LT | 1 |
| SE | 1 |
| TR | 1 |
| MD | 1 |
| CZ | 1 |
| IN | 1 |
| ID | 1 |
| KH | 1 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 43.08 | 63 | 309 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 39.67 | 48 | 340 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 21.09 | 158 | 604 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.41 | 226 | 259 |
| 5 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 12.74 | 283 | 318 |
| 6 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.41 | 246 | 238 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.40 | 272 | 312 |
| 8 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 12.27 | 261 | 337 |
| 9 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 12.08 | 253 | 299 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 12.01 | 250 | 339 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
