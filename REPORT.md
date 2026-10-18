# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T09:07:12Z** UTC (прогон занял 51 с)

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
| Разобрано в конфиги | 141 |
| Уникальных | 141 |
| Endpoint отвечает по TCP | 128 |
| YouTube доступен | 79 |
| + Telegram (HTTP) доступен | 66 |
| + дата-центр Telegram доступен | 66 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 33 |
| shadowsocks | 4 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 5 |
| DE | 5 |
| NL | 4 |
| US | 3 |
| PL | 3 |
| HK | 3 |
| FI | 2 |
| SE | 2 |
| AT | 1 |
| IT | 1 |
| CZ | 1 |
| LT | 1 |
| EE | 1 |
| BY | 1 |
| TR | 1 |
| ID | 1 |
| MD | 1 |
| IN | 1 |
| KH | 1 |
| FR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 28.67 | 55 | 364 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 22.66 | 133 | 626 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.02 | 280 | 592 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 11.01 | 264 | 266 |
| 5 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 10.88 | 271 | 311 |
| 6 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 10.73 | 323 | 352 |
| 7 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 10.72 | 295 | 350 |
| 8 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 10.30 | 336 | 597 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.23 | 297 | 352 |
| 10 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.88 | 270 | 1008 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
