# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-12T23:00:01Z** UTC (прогон занял 47 с)

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
| Строк в источниках | 445 |
| Разобрано в конфиги | 397 |
| Уникальных | 397 |
| Endpoint отвечает по TCP | 388 |
| YouTube доступен | 276 |
| + Telegram (HTTP) доступен | 266 |
| + дата-центр Telegram доступен | 266 |
| + скорость ≥ 3.0 Мбит/с | 162 |
| **В итоговом списке** | **162** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 81 |
| vmess | 45 |
| shadowsocks | 36 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 71 |
| CA | 32 |
| IT | 13 |
| ?? | 8 |
| DE | 7 |
| NL | 7 |
| FR | 7 |
| ES | 4 |
| GB | 3 |
| SE | 3 |
| PL | 3 |
| CH | 1 |
| LV | 1 |
| TR | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 31.21 | 40 | 629 |
| 2 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 23.74 | 46 | 664 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 22.66 | 12 | 332 |
| 4 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 21.48 | 31 | 622 |
| 5 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 21.44 | 29 | 620 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 21.17 | 18 | 308 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 20.00 | 29 | 328 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 19.55 | 71 | 384 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 18.78 | 40 | 742 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 18.36 | 94 | 362 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 44 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
