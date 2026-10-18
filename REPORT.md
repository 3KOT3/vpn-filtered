# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T05:36:09Z** UTC (прогон занял 53 с)

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
| Endpoint отвечает по TCP | 139 |
| YouTube доступен | 108 |
| + Telegram (HTTP) доступен | 102 |
| + дата-центр Telegram доступен | 102 |
| + скорость ≥ 3.0 Мбит/с | 54 |
| **В итоговом списке** | **54** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 42 |
| vmess | 5 |
| trojan | 4 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 7 |
| PH | 7 |
| US | 5 |
| JP | 5 |
| NL | 4 |
| HK | 3 |
| PL | 3 |
| FI | 3 |
| SG | 3 |
| EE | 2 |
| IN | 2 |
| IT | 1 |
| AT | 1 |
| LT | 1 |
| LV | 1 |
| SE | 1 |
| MD | 1 |
| ID | 1 |
| MY | 1 |
| KR | 1 |
| KH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 39.63 | 37 | 343 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 37.96 | 39 | 309 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.57 | 406 | 747 |
| 4 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 14.19 | 235 | 311 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.04 | 206 | 217 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.93 | 190 | 677 |
| 7 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 13.77 | 211 | 258 |
| 8 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 13.75 | 224 | 267 |
| 9 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.27 | 266 | 290 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.11 | 239 | 265 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
