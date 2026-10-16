# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T17:04:12Z** UTC (прогон занял 51 с)

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
| YouTube доступен | 83 |
| + Telegram (HTTP) доступен | 77 |
| + дата-центр Telegram доступен | 77 |
| + скорость ≥ 2.0 Мбит/с | 48 |
| **В итоговом списке** | **48** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 36 |
| trojan | 7 |
| vmess | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 26 |
| BR | 5 |
| US | 2 |
| ES | 2 |
| DE | 2 |
| HK | 2 |
| SG | 2 |
| FI | 1 |
| IT | 1 |
| UA | 1 |
| TR | 1 |
| JP | 1 |
| ZA | 1 |
| ID | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 37.18 | 77 | 294 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 28.99 | 59 | 367 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 26.78 | 173 | 553 |
| 4 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 25.05 | 105 | 859 |
| 5 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 24.88 | 306 | 641 |
| 6 |  | vmess | ?? | 23.61 | 197 | 437 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 21.04 | 140 | 584 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.80 | 242 | 270 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.29 | 315 | 289 |
| 10 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.16 | 305 | 626 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
