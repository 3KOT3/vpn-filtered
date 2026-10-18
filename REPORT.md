# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:31:04Z** UTC (прогон занял 43 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 120 |
| Уникальных | 120 |
| Endpoint отвечает по TCP | 101 |
| YouTube доступен | 61 |
| + Telegram (HTTP) доступен | 56 |
| + дата-центр Telegram доступен | 56 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 28 |
| vmess | 9 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 11 |
| PL | 4 |
| JP | 3 |
| KR | 3 |
| DE | 3 |
| US | 2 |
| HK | 2 |
| BR | 1 |
| IT | 1 |
| CZ | 1 |
| LT | 1 |
| NL | 1 |
| BY | 1 |
| MY | 1 |
| IN | 1 |
| SE | 1 |
| AU | 1 |
| PH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.35 | 131 | 436 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.43 | 263 | 528 |
| 3 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.71 | 217 | 973 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 8.63 | 212 | 985 |
| 5 | 🇧🇷[openproxylist.com] vless-BR | vless | BR | 8.44 | 214 | 964 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 6.89 | 317 | 332 |
| 7 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 6.67 | 347 | 387 |
| 8 | 🇰🇷[openproxylist.com] vmess-KR | vmess | KR | 6.54 | 463 | 1012 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 6.41 | 734 | 379 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 6.35 | 342 | 420 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
