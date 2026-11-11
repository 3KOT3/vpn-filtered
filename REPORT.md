# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-11T23:52:53Z** UTC (прогон занял 51 с)

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
| Строк в источниках | 448 |
| Разобрано в конфиги | 392 |
| Уникальных | 392 |
| Endpoint отвечает по TCP | 388 |
| YouTube доступен | 277 |
| + Telegram (HTTP) доступен | 261 |
| + дата-центр Telegram доступен | 261 |
| + скорость ≥ 3.0 Мбит/с | 128 |
| **В итоговом списке** | **128** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 54 |
| shadowsocks | 51 |
| vless | 23 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 72 |
| CA | 12 |
| IT | 10 |
| NL | 9 |
| DE | 8 |
| FR | 5 |
| GB | 3 |
| ES | 3 |
| CH | 2 |
| SE | 2 |
| FI | 1 |
| BY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.81 | 66 | 291 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 15.55 | 46 | 394 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 11.85 | 54 | 289 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.85 | 28 | 310 |
| 5 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 11.70 | 67 | 287 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.48 | 123 | 434 |
| 7 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 9.93 | 88 | 432 |
| 8 | [🇨🇦] [vm-no-ra] [261111-232839.560] | vmess | CA | 9.86 | 80 | 299 |
| 9 | [🇺🇸] [vm-no-ra] [261111-232822.891] | vmess | US | 9.73 | 81 | 296 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.64 | 84 | 455 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 54 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
