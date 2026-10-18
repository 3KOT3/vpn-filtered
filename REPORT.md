# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T05:58:30Z** UTC (прогон занял 48 с)

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
| Endpoint отвечает по TCP | 134 |
| YouTube доступен | 98 |
| + Telegram (HTTP) доступен | 88 |
| + дата-центр Telegram доступен | 88 |
| + скорость ≥ 3.0 Мбит/с | 47 |
| **В итоговом списке** | **47** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 40 |
| shadowsocks | 4 |
| vmess | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 7 |
| JP | 5 |
| PH | 5 |
| US | 4 |
| NL | 4 |
| HK | 4 |
| FI | 3 |
| PL | 2 |
| AT | 1 |
| IT | 1 |
| EE | 1 |
| LT | 1 |
| TR | 1 |
| MD | 1 |
| KH | 1 |
| ID | 1 |
| LV | 1 |
| IN | 1 |
| RU | 1 |
| SE | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 55.51 | 35 | 333 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.18 | 184 | 680 |
| 3 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 15.87 | 195 | 209 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.86 | 233 | 294 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.77 | 341 | 667 |
| 6 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 14.51 | 217 | 255 |
| 7 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 14.41 | 266 | 307 |
| 8 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 14.26 | 232 | 280 |
| 9 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 14.09 | 217 | 307 |
| 10 | 🇩🇪[openproxylist.com] vmess-DE | vmess | DE | 13.99 | 195 | 219 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
