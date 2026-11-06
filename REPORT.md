# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-06T22:33:20Z** UTC (прогон занял 54 с)

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
| Строк в источниках | 447 |
| Разобрано в конфиги | 428 |
| Уникальных | 428 |
| Endpoint отвечает по TCP | 421 |
| YouTube доступен | 233 |
| + Telegram (HTTP) доступен | 214 |
| + дата-центр Telegram доступен | 214 |
| + скорость ≥ 3.0 Мбит/с | 77 |
| **В итоговом списке** | **77** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 35 |
| shadowsocks | 19 |
| trojan | 18 |
| vless | 5 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 57 |
| CA | 17 |
| ES | 1 |
| GB | 1 |
| DE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | [🇺🇸] [vm-no-ra] [261106-232036.498] | vmess | US | 16.92 | 76 | 565 |
| 2 | [🇺🇸] [vl-re-ra] [261106-231419.349] | vless | US | 12.59 | 26 | 490 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 11.59 | 56 | 529 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.42 | 23 | 612 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 10.92 | 29 | 432 |
| 6 | [🇺🇸] [vl-re-ra] [261106-231539.737] | vless | US | 9.72 | 31 | 460 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.71 | 75 | 493 |
| 8 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 7.01 | 92 | 446 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 6.93 | 32 | 489 |
| 10 | [🇺🇸] [vm-no-ra] [261106-232059.694] | vmess | US | 6.86 | 50 | 448 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 4 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
