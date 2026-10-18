# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T08:46:58Z** UTC (прогон занял 43 с)

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
| Endpoint отвечает по TCP | 130 |
| YouTube доступен | 84 |
| + Telegram (HTTP) доступен | 63 |
| + дата-центр Telegram доступен | 63 |
| + скорость ≥ 3.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 31 |
| shadowsocks | 4 |
| vmess | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 5 |
| NL | 5 |
| JP | 5 |
| US | 4 |
| HK | 3 |
| PL | 2 |
| FI | 2 |
| SE | 2 |
| IT | 1 |
| AT | 1 |
| LT | 1 |
| CZ | 1 |
| BY | 1 |
| EE | 1 |
| MD | 1 |
| TR | 1 |
| IN | 1 |
| ID | 1 |
| MY | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 35.64 | 41 | 362 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.43 | 184 | 694 |
| 3 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 14.90 | 226 | 276 |
| 4 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 14.70 | 223 | 268 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.80 | 214 | 236 |
| 6 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 13.65 | 221 | 265 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.57 | 229 | 321 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 12.89 | 255 | 292 |
| 9 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 12.21 | 233 | 326 |
| 10 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 12.17 | 220 | 307 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
