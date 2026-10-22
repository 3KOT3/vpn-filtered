# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-22T02:33:41Z** UTC (прогон занял 51 с)

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
| Строк в источниках | 404 |
| Разобрано в конфиги | 380 |
| Уникальных | 380 |
| Endpoint отвечает по TCP | 367 |
| YouTube доступен | 252 |
| + Telegram (HTTP) доступен | 235 |
| + дата-центр Telegram доступен | 235 |
| + скорость ≥ 3.0 Мбит/с | 70 |
| **В итоговом списке** | **70** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 38 |
| shadowsocks | 13 |
| vmess | 13 |
| trojan | 6 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 23 |
| CA | 16 |
| DE | 9 |
| GB | 7 |
| NL | 5 |
| CL | 4 |
| IT | 2 |
| AT | 1 |
| LV | 1 |
| PL | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 15.80 | 28 | 401 |
| 2 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 15.40 | 30 | 417 |
| 3 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 15.26 | 62 | 407 |
| 4 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 15.25 | 31 | 419 |
| 5 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 14.16 | 28 | 430 |
| 6 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 14.16 | 23 | 449 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.44 | 15 | 278 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.29 | 39 | 334 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 12.52 | 32 | 418 |
| 10 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 12.05 | 29 | 401 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 8 |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
