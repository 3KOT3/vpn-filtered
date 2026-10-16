# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T15:40:10Z** UTC (прогон занял 62 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 133 |
| Уникальных | 133 |
| Endpoint отвечает по TCP | 118 |
| YouTube доступен | 85 |
| + Telegram (HTTP) доступен | 74 |
| + дата-центр Telegram доступен | 74 |
| + скорость ≥ 2.0 Мбит/с | 48 |
| **В итоговом списке** | **48** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 36 |
| vmess | 5 |
| trojan | 5 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 26 |
| BR | 5 |
| DE | 3 |
| US | 2 |
| ES | 2 |
| IT | 1 |
| FI | 1 |
| HK | 1 |
| TR | 1 |
| ZA | 1 |
| ID | 1 |
| IN | 1 |
| UA | 1 |
| SG | 1 |
| JP | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 41.96 | 38 | 328 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 40.27 | 56 | 663 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 37.74 | 42 | 328 |
| 4 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 35.12 | 55 | 572 |
| 5 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 30.80 | 57 | 754 |
| 6 |  | vmess | ?? | 29.58 | 136 | 355 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 17.55 | 202 | 227 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 17.52 | 184 | 716 |
| 9 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 14.66 | 265 | 293 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.45 | 208 | 238 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
