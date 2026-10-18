# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T05:48:31Z** UTC (прогон занял 42 с)

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
| Endpoint отвечает по TCP | 139 |
| YouTube доступен | 111 |
| + Telegram (HTTP) доступен | 98 |
| + дата-центр Telegram доступен | 98 |
| + скорость ≥ 3.0 Мбит/с | 50 |
| **В итоговом списке** | **50** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 43 |
| shadowsocks | 3 |
| vmess | 3 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| PH | 7 |
| US | 5 |
| DE | 5 |
| NL | 5 |
| JP | 5 |
| HK | 4 |
| PL | 3 |
| FI | 3 |
| IT | 1 |
| AT | 1 |
| EE | 1 |
| LT | 1 |
| LV | 1 |
| SE | 1 |
| TR | 1 |
| KH | 1 |
| MD | 1 |
| ID | 1 |
| SG | 1 |
| IN | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 53.14 | 43 | 252 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 38.06 | 40 | 329 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.73 | 185 | 694 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.28 | 202 | 232 |
| 5 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 14.20 | 462 | 346 |
| 6 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.08 | 234 | 258 |
| 7 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 14.05 | 223 | 270 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.95 | 245 | 289 |
| 9 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 13.60 | 270 | 344 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 13.33 | 221 | 322 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
