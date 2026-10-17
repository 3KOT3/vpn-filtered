# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T14:54:44Z** UTC (прогон занял 36 с)

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
| Строк в источниках | 145 |
| Разобрано в конфиги | 129 |
| Уникальных | 129 |
| Endpoint отвечает по TCP | 119 |
| YouTube доступен | 84 |
| + Telegram (HTTP) доступен | 72 |
| + дата-центр Telegram доступен | 72 |
| + скорость ≥ 3.0 Мбит/с | 35 |
| **В итоговом списке** | **35** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 29 |
| vmess | 3 |
| shadowsocks | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 16 |
| FI | 3 |
| PL | 2 |
| JP | 2 |
| NL | 2 |
| US | 1 |
| ID | 1 |
| EE | 1 |
| LT | 1 |
| TR | 1 |
| DE | 1 |
| BR | 1 |
| IN | 1 |
| TW | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 33.39 | 65 | 515 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 16.55 | 159 | 432 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 11.27 | 699 | 967 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.58 | 333 | 358 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 9.39 | 342 | 423 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.33 | 384 | 401 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 9.09 | 333 | 422 |
| 8 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.91 | 354 | 416 |
| 9 | 🇮🇩[openproxylist.com] vless-ID | vless | ID | 8.89 | 563 | 910 |
| 10 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.81 | 365 | 1089 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
