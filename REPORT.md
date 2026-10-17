# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T20:11:27Z** UTC (прогон занял 38 с)

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
| Разобрано в конфиги | 106 |
| Уникальных | 106 |
| Endpoint отвечает по TCP | 103 |
| YouTube доступен | 64 |
| + Telegram (HTTP) доступен | 57 |
| + дата-центр Telegram доступен | 57 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 33 |
| vmess | 3 |
| shadowsocks | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 15 |
| BR | 5 |
| PH | 3 |
| US | 2 |
| NL | 2 |
| FI | 2 |
| AT | 1 |
| PL | 1 |
| HU | 1 |
| SE | 1 |
| EE | 1 |
| MD | 1 |
| IN | 1 |
| JP | 1 |
| SG | 1 |
| KH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 34.75 | 40 | 330 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 34.04 | 60 | 304 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.71 | 184 | 684 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 14.31 | 227 | 278 |
| 5 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.58 | 274 | 319 |
| 6 | 🏳[openproxylist.com] vmess- | vmess | ?? | 13.57 | 205 | 234 |
| 7 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 13.28 | 223 | 326 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 13.24 | 217 | 313 |
| 9 | 🏳[openproxylist.com] vless- | vless | ?? | 13.06 | 255 | 328 |
| 10 | 🇳🇱[openproxylist.com] vmess-NL | vmess | NL | 12.89 | 459 | 375 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
