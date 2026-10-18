# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T05:43:10Z** UTC (прогон занял 38 с)

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
| + Telegram (HTTP) доступен | 98 |
| + дата-центр Telegram доступен | 98 |
| + скорость ≥ 3.0 Мбит/с | 51 |
| **В итоговом списке** | **51** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 43 |
| vmess | 4 |
| shadowsocks | 3 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 7 |
| PH | 7 |
| US | 5 |
| NL | 5 |
| FI | 4 |
| JP | 4 |
| HK | 4 |
| PL | 3 |
| AT | 1 |
| IT | 1 |
| EE | 1 |
| FR | 1 |
| LT | 1 |
| TR | 1 |
| SE | 1 |
| MD | 1 |
| IN | 1 |
| ID | 1 |
| MY | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 52.57 | 39 | 285 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 37.32 | 36 | 326 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 17.36 | 187 | 771 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.30 | 191 | 233 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.94 | 339 | 659 |
| 6 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.77 | 320 | 348 |
| 7 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.77 | 253 | 297 |
| 8 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 13.69 | 223 | 277 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.49 | 234 | 275 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.21 | 244 | 260 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
