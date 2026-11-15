# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-15T22:18:45Z** UTC (прогон занял 44 с)

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
| Строк в источниках | 444 |
| Разобрано в конфиги | 394 |
| Уникальных | 394 |
| Endpoint отвечает по TCP | 389 |
| YouTube доступен | 222 |
| + Telegram (HTTP) доступен | 201 |
| + дата-центр Telegram доступен | 201 |
| + скорость ≥ 3.0 Мбит/с | 88 |
| **В итоговом списке** | **88** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 34 |
| vmess | 30 |
| vless | 22 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 33 |
| CA | 14 |
| IT | 7 |
| DE | 6 |
| FR | 6 |
| ES | 5 |
| GB | 4 |
| FI | 4 |
| CH | 3 |
| SE | 3 |
| NL | 2 |
| TR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 21.79 | 39 | 345 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 20.91 | 38 | 332 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 17.80 | 58 | 279 |
| 4 | [🇺🇸] [vm-no-ra] [261115-200951.615] | vmess | US | 15.42 | 67 | 269 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.87 | 39 | 339 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.15 | 87 | 422 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 12.06 | 109 | 386 |
| 8 | [🇺🇸] [vm-no-ra] [261115-201038.131] | vmess | US | 11.26 | 115 | 448 |
| 9 | [🇺🇸] [vm-no-ra] [261115-201038.168] | vmess | US | 11.07 | 151 | 435 |
| 10 | [🇺🇸] [vm-no-ra] [261115-201038.278] | vmess | US | 10.92 | 113 | 425 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 40 |
| vmess-http-obfs | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
