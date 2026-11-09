# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-09T03:45:49Z** UTC (прогон занял 70 с)

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
| Строк в источниках | 446 |
| Разобрано в конфиги | 406 |
| Уникальных | 406 |
| Endpoint отвечает по TCP | 401 |
| YouTube доступен | 298 |
| + Telegram (HTTP) доступен | 277 |
| + дата-центр Telegram доступен | 277 |
| + скорость ≥ 3.0 Мбит/с | 179 |
| **В итоговом списке** | **179** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 63 |
| shadowsocks | 59 |
| vmess | 56 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 125 |
| CA | 16 |
| DE | 13 |
| FR | 6 |
| ES | 4 |
| GB | 3 |
| CH | 3 |
| ?? | 2 |
| JP | 2 |
| NL | 2 |
| SE | 1 |
| IT | 1 |
| BY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.82 | 55 | 472 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.84 | 36 | 484 |
| 3 | [🇺🇸] [vl-re-ra] [261109-015923.599] | vless | US | 14.67 | 27 | 467 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.35 | 71 | 416 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.05 | 67 | 436 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.81 | 58 | 475 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.45 | 83 | 501 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.55 | 41 | 441 |
| 9 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.53 | 70 | 527 |
| 10 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.33 | 92 | 475 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 32 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
