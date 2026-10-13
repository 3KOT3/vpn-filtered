# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-13T13:03:53Z** UTC (прогон занял 124 с)

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
| Строк в источниках | 149 |
| Разобрано в конфиги | 140 |
| Уникальных | 140 |
| Endpoint отвечает по TCP | 136 |
| YouTube доступен | 95 |
| + Telegram (HTTP) доступен | 80 |
| + дата-центр Telegram доступен | 80 |
| + скорость ≥ 2.0 Мбит/с | 48 |
| **В итоговом списке** | **48** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 30 |
| vless | 15 |
| vmess | 2 |
| shadowsocks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 15 |
| KR | 7 |
| NL | 5 |
| SG | 5 |
| ?? | 4 |
| EE | 3 |
| US | 2 |
| PL | 2 |
| AT | 1 |
| IE | 1 |
| TR | 1 |
| FI | 1 |
| LV | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 27.18 | 163 | 1938 |
| 2 | 🏳[openproxylist.com] trojan- | trojan | ?? | 16.12 | 149 | 234 |
| 3 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 15.36 | 206 | 202 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.31 | 196 | 191 |
| 5 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 13.97 | 194 | 196 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 13.57 | 200 | 200 |
| 7 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 13.54 | 204 | 193 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 13.47 | 218 | 210 |
| 9 | 🇪🇪[openproxylist.com] vless-EE | vless | EE | 13.36 | 272 | 470 |
| 10 | 🇪🇪[openproxylist.com] vless-EE | vless | EE | 12.94 | 228 | 325 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
