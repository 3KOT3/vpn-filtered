# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T17:02:12Z** UTC (прогон занял 47 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 147 |
| Разобрано в конфиги | 111 |
| Уникальных | 111 |
| Endpoint отвечает по TCP | 107 |
| YouTube доступен | 73 |
| + Telegram (HTTP) доступен | 60 |
| + дата-центр Telegram доступен | 60 |
| + скорость ≥ 3.0 Мбит/с | 34 |
| **В итоговом списке** | **34** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 28 |
| vmess | 4 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 12 |
| PL | 4 |
| FI | 3 |
| JP | 3 |
| US | 2 |
| NL | 2 |
| HU | 1 |
| DE | 1 |
| EE | 1 |
| TR | 1 |
| BR | 1 |
| KR | 1 |
| IN | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 34.03 | 40 | 347 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 14.73 | 53 | 337 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.01 | 198 | 689 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.54 | 343 | 770 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 13.22 | 210 | 226 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 13.01 | 237 | 342 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.98 | 254 | 288 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.62 | 225 | 299 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.57 | 233 | 272 |
| 10 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.51 | 233 | 276 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
