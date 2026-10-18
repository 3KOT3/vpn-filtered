# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T17:13:12Z** UTC (прогон занял 46 с)

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
| Разобрано в конфиги | 72 |
| Уникальных | 72 |
| Endpoint отвечает по TCP | 69 |
| YouTube доступен | 41 |
| + Telegram (HTTP) доступен | 35 |
| + дата-центр Telegram доступен | 35 |
| + скорость ≥ 3.0 Мбит/с | 21 |
| **В итоговом списке** | **21** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 19 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 7 |
| JP | 4 |
| US | 2 |
| PL | 2 |
| DE | 2 |
| CA | 1 |
| NL | 1 |
| BR | 1 |
| EE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 20.51 | 91 | 361 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.96 | 136 | 641 |
| 3 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 9.15 | 261 | 312 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 8.47 | 301 | 712 |
| 5 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 8.45 | 293 | 326 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 8.35 | 237 | 281 |
| 7 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.18 | 271 | 333 |
| 8 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.47 | 287 | 1047 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 7.47 | 298 | 360 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 7.26 | 282 | 1013 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 68 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
