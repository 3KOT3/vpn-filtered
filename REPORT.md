# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-29T18:10:03Z** UTC (прогон занял 46 с)

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
| Строк в источниках | 392 |
| Разобрано в конфиги | 359 |
| Уникальных | 359 |
| Endpoint отвечает по TCP | 345 |
| YouTube доступен | 205 |
| + Telegram (HTTP) доступен | 175 |
| + дата-центр Telegram доступен | 175 |
| + скорость ≥ 3.0 Мбит/с | 50 |
| **В итоговом списке** | **50** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 23 |
| vmess | 17 |
| trojan | 7 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| CA | 20 |
| US | 16 |
| ?? | 5 |
| GB | 2 |
| ES | 2 |
| NL | 1 |
| IT | 1 |
| AT | 1 |
| CH | 1 |
| DE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] trojan- | trojan | ?? | 11.52 | 66 | 358 |
| 2 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.14 | 81 | 407 |
| 3 | 🏳[openproxylist.com] trojan- | trojan | ?? | 10.57 | 80 | 407 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 10.35 | 82 | 394 |
| 5 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 10.16 | 104 | 681 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 10.10 | 69 | 427 |
| 7 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 9.94 | 107 | 721 |
| 8 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 9.64 | 181 | 870 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 9.26 | 158 | 747 |
| 10 | [🇨🇦] [vm-no-ra] [261029-171342.928] | vmess | CA | 9.19 | 2287 | 334 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 16 |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
