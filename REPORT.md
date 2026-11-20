# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-20T00:02:53Z** UTC (прогон занял 42 с)

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
| Строк в источниках | 428 |
| Разобрано в конфиги | 382 |
| Уникальных | 382 |
| Endpoint отвечает по TCP | 365 |
| YouTube доступен | 268 |
| + Telegram (HTTP) доступен | 241 |
| + дата-центр Telegram доступен | 241 |
| + скорость ≥ 3.0 Мбит/с | 99 |
| **В итоговом списке** | **99** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 40 |
| vmess | 38 |
| vless | 19 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 35 |
| CA | 13 |
| IT | 10 |
| ?? | 8 |
| FR | 8 |
| DE | 6 |
| NL | 6 |
| ES | 3 |
| GB | 3 |
| JP | 2 |
| FI | 2 |
| MX | 1 |
| AT | 1 |
| SE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 18.03 | 58 | 375 |
| 2 | 🇲🇽[openproxylist.com] ss-MX | shadowsocks | MX | 11.30 | 101 | 697 |
| 3 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.06 | 192 | 456 |
| 4 | 🏳[openproxylist.com] vmess- | vmess | ?? | 10.97 | 104 | 394 |
| 5 | [🇺🇸] [vl-re-ra] [261119-153703.435] | vless | US | 10.77 | 87 | 469 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.45 | 86 | 519 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 10.31 | 106 | 515 |
| 8 | [🇺🇸] [vm-no-ra] [261119-154035.622] | vmess | US | 9.59 | 142 | 363 |
| 9 | [🇺🇸] [vl-re-ra] [261119-153257.933] | vless | US | 9.36 | 95 | 361 |
| 10 | [🇺🇸] [vm-no-ra] [261119-154035.475] | vmess | US | 9.29 | 121 | 368 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 38 |
| vmess-http-obfs | 1 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
