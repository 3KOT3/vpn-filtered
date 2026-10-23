# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-23T02:38:22Z** UTC (прогон занял 49 с)

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
| Строк в источниках | 399 |
| Разобрано в конфиги | 373 |
| Уникальных | 373 |
| Endpoint отвечает по TCP | 337 |
| YouTube доступен | 210 |
| + Telegram (HTTP) доступен | 200 |
| + дата-центр Telegram доступен | 200 |
| + скорость ≥ 3.0 Мбит/с | 54 |
| **В итоговом списке** | **54** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 22 |
| vmess | 17 |
| shadowsocks | 13 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 23 |
| CA | 19 |
| GB | 4 |
| IT | 3 |
| NL | 2 |
| DE | 1 |
| AT | 1 |
| ?? | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 8.31 | 122 | 320 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 8.14 | 81 | 332 |
| 3 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 7.40 | 119 | 719 |
| 4 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 7.17 | 113 | 771 |
| 5 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 6.95 | 85 | 666 |
| 6 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 6.84 | 120 | 765 |
| 7 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 6.78 | 257 | 779 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 6.55 | 132 | 482 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 6.51 | 114 | 676 |
| 10 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 6.48 | 263 | 851 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 6 |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
