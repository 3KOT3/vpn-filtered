# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T16:53:33Z** UTC (прогон занял 29 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 148 |
| Разобрано в конфиги | 50 |
| Уникальных | 50 |
| Endpoint отвечает по TCP | 45 |
| YouTube доступен | 29 |
| + Telegram (HTTP) доступен | 27 |
| + дата-центр Telegram доступен | 27 |
| + скорость ≥ 2.0 Мбит/с | 19 |
| **В итоговом списке** | **19** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 15 |
| shadowsocks | 2 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 9 |
| JP | 3 |
| PL | 2 |
| DE | 2 |
| US | 1 |
| NL | 1 |
| BR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 11.95 | 291 | 704 |
| 2 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 9.01 | 266 | 337 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 8.26 | 298 | 450 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 8.17 | 289 | 337 |
| 5 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.17 | 288 | 341 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 7.95 | 317 | 381 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 7.70 | 280 | 1024 |
| 8 | 🇩🇪[openproxylist.com] vmess-DE | vmess | DE | 7.64 | 261 | 374 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 7.50 | 308 | 351 |
| 10 | 🏳[openproxylist.com] vmess- | vmess | ?? | 7.43 | 279 | 995 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 90 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
