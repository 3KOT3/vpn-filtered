# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-15T20:37:02Z** UTC (прогон занял 64 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 147 |
| Разобрано в конфиги | 132 |
| Уникальных | 132 |
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 76 |
| + Telegram (HTTP) доступен | 59 |
| + дата-центр Telegram доступен | 59 |
| + скорость ≥ 2.0 Мбит/с | 34 |
| **В итоговом списке** | **34** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 24 |
| trojan | 7 |
| shadowsocks | 2 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 7 |
| US | 3 |
| DE | 3 |
| FI | 3 |
| SG | 3 |
| HK | 2 |
| JP | 2 |
| IT | 1 |
| AT | 1 |
| KH | 1 |
| CA | 1 |
| ES | 1 |
| UA | 1 |
| TR | 1 |
| KR | 1 |
| BR | 1 |
| PL | 1 |
| NL | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 26.51 | 131 | 423 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.50 | 104 | 630 |
| 3 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.82 | 327 | 359 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.89 | 269 | 585 |
| 5 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 9.45 | 323 | 379 |
| 6 | 🏳[openproxylist.com] vless- | vless | ?? | 9.03 | 300 | 335 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 8.98 | 1735 | 1573 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 8.63 | 358 | 399 |
| 9 | 🇰🇭[openproxylist.com] vless-KH | vless | KH | 8.60 | 297 | 294 |
| 10 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 8.60 | 332 | 422 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
