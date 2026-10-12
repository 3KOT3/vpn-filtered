# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-12T23:53:18Z** UTC (прогон занял 62 с)

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
| Разобрано в конфиги | 136 |
| Уникальных | 136 |
| Endpoint отвечает по TCP | 136 |
| YouTube доступен | 117 |
| + Telegram (HTTP) доступен | 111 |
| + дата-центр Telegram доступен | 111 |
| + скорость ≥ 2.0 Мбит/с | 77 |
| **В итоговом списке** | **77** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 38 |
| vless | 33 |
| shadowsocks | 4 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 14 |
| KR | 9 |
| SG | 9 |
| DE | 8 |
| PL | 6 |
| US | 5 |
| NL | 5 |
| ?? | 4 |
| FI | 3 |
| IE | 2 |
| LV | 2 |
| GB | 2 |
| FR | 1 |
| AT | 1 |
| EE | 1 |
| TR | 1 |
| SE | 1 |
| KZ | 1 |
| TW | 1 |
| TH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 23.31 | 136 | 694 |
| 2 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 13.68 | 204 | 281 |
| 3 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 13.22 | 239 | 273 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 13.10 | 251 | 276 |
| 5 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 12.99 | 240 | 253 |
| 6 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.84 | 243 | 284 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.82 | 242 | 275 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.30 | 246 | 247 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 11.98 | 245 | 248 |
| 10 | 🇩🇪[openproxylist.com] trojan-DE | trojan | DE | 11.88 | 259 | 341 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
