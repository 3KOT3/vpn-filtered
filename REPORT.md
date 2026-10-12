# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-12T13:40:25Z** UTC (прогон занял 55 с)

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
| Разобрано в конфиги | 142 |
| Уникальных | 142 |
| Endpoint отвечает по TCP | 134 |
| YouTube доступен | 104 |
| + Telegram (HTTP) доступен | 94 |
| + дата-центр Telegram доступен | 94 |
| + скорость ≥ 2.0 Мбит/с | 72 |
| **В итоговом списке** | **72** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 47 |
| vless | 22 |
| vmess | 2 |
| shadowsocks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 14 |
| KR | 14 |
| SG | 11 |
| DE | 6 |
| US | 5 |
| ?? | 5 |
| PL | 4 |
| NL | 3 |
| FI | 3 |
| FR | 2 |
| IE | 2 |
| GB | 1 |
| EE | 1 |
| SE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 21.67 | 72 | 1341 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 15.50 | 132 | 633 |
| 3 | 🇬🇧[openproxylist.com] vless-GB | vless | GB | 11.37 | 226 | 259 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 10.94 | 247 | 250 |
| 5 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 10.67 | 245 | 274 |
| 6 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 10.54 | 211 | 285 |
| 7 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 10.26 | 236 | 237 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 10.02 | 249 | 282 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 9.98 | 234 | 239 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.79 | 281 | 313 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
