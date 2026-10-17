# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T14:57:57Z** UTC (прогон занял 36 с)

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
| Endpoint отвечает по TCP | 114 |
| YouTube доступен | 81 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 3.0 Мбит/с | 31 |
| **В итоговом списке** | **31** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 26 |
| vmess | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 15 |
| FI | 3 |
| PL | 2 |
| NL | 2 |
| US | 1 |
| HU | 1 |
| LT | 1 |
| TR | 1 |
| BR | 1 |
| DE | 1 |
| JP | 1 |
| IN | 1 |
| EE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 16.46 | 91 | 367 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.94 | 133 | 586 |
| 3 | 🏳[openproxylist.com] vless- | vless | ?? | 10.06 | 270 | 347 |
| 4 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 9.69 | 280 | 325 |
| 5 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.41 | 293 | 339 |
| 6 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 9.35 | 266 | 316 |
| 7 | 🏳[openproxylist.com] vless- | vless | ?? | 9.27 | 260 | 361 |
| 8 | 🇳🇱[openproxylist.com] vmess-NL | vmess | NL | 9.04 | 347 | 305 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.86 | 272 | 332 |
| 10 | 🇭🇺[openproxylist.com] vless-HU | vless | HU | 8.78 | 303 | 328 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
