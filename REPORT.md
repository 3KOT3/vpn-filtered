# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T16:49:24Z** UTC (прогон занял 49 с)

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
| Endpoint отвечает по TCP | 123 |
| YouTube доступен | 82 |
| + Telegram (HTTP) доступен | 73 |
| + дата-центр Telegram доступен | 73 |
| + скорость ≥ 2.0 Мбит/с | 50 |
| **В итоговом списке** | **50** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 37 |
| trojan | 6 |
| vmess | 4 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 27 |
| BR | 7 |
| DE | 3 |
| ES | 2 |
| US | 1 |
| UA | 1 |
| FI | 1 |
| IT | 1 |
| HK | 1 |
| TR | 1 |
| JP | 1 |
| ZA | 1 |
| ID | 1 |
| IN | 1 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 17.83 | 131 | 561 |
| 2 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 17.65 | 106 | 592 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 17.21 | 109 | 597 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 16.37 | 76 | 366 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 15.60 | 133 | 637 |
| 6 |  | vmess | ?? | 14.22 | 212 | 406 |
| 7 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.17 | 315 | 908 |
| 8 | 🇺🇦[openproxylist.com] vless-UA | vless | UA | 10.86 | 399 | 315 |
| 9 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 10.51 | 290 | 370 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.36 | 305 | 335 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
