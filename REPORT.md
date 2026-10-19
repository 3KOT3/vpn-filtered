# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-19T14:21:05Z** UTC (прогон занял 40 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **1.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 149 |
| Разобрано в конфиги | 147 |
| Уникальных | 147 |
| Endpoint отвечает по TCP | 138 |
| YouTube доступен | 82 |
| + Telegram (HTTP) доступен | 76 |
| + дата-центр Telegram доступен | 76 |
| + скорость ≥ 1.0 Мбит/с | 53 |
| **В итоговом списке** | **53** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 48 |
| shadowsocks | 4 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 9 |
| ?? | 7 |
| US | 5 |
| DE | 5 |
| FI | 5 |
| PH | 2 |
| PL | 2 |
| IT | 2 |
| HU | 2 |
| SE | 2 |
| NL | 2 |
| AT | 1 |
| GB | 1 |
| UA | 1 |
| LV | 1 |
| CZ | 1 |
| RU | 1 |
| TR | 1 |
| SG | 1 |
| EE | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 13.06 | 48 | 662 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.50 | 110 | 596 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 10.80 | 171 | 477 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.29 | 152 | 382 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.27 | 181 | 435 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 8.17 | 162 | 440 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 8.00 | 52 | 680 |
| 8 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.67 | 237 | 979 |
| 9 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.39 | 232 | 977 |
| 10 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.37 | 232 | 991 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
