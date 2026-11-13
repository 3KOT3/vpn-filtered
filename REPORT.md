# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-13T13:40:35Z** UTC (прогон занял 62 с)

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
| Разобрано в конфиги | 409 |
| Уникальных | 409 |
| Endpoint отвечает по TCP | 395 |
| YouTube доступен | 201 |
| + Telegram (HTTP) доступен | 184 |
| + дата-центр Telegram доступен | 184 |
| + скорость ≥ 3.0 Мбит/с | 94 |
| **В итоговом списке** | **94** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 37 |
| vless | 34 |
| shadowsocks | 23 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 38 |
| CA | 31 |
| ?? | 5 |
| IT | 4 |
| DE | 3 |
| EE | 2 |
| FR | 2 |
| ES | 2 |
| SE | 2 |
| NL | 2 |
| CH | 1 |
| GB | 1 |
| TR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 14.17 | 46 | 265 |
| 2 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 13.59 | 43 | 268 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 10.20 | 105 | 323 |
| 4 | [🇨🇦] [vm-no-ra] [261113-054408.669] | vmess | CA | 7.71 | 79 | 340 |
| 5 | [🇨🇦] [vm-no-ra] [261113-054408.791] | vmess | CA | 7.59 | 77 | 336 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 7.23 | 63 | 330 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 7.05 | 82 | 394 |
| 8 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 6.71 | 129 | 415 |
| 9 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 6.67 | 98 | 401 |
| 10 | 🌐 Anycast-IP | 🇨🇦 🇫🇮 | [BL] | vless | CA | 6.39 | 47 | 452 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 32 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
