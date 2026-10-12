# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-12T02:51:44Z** UTC (прогон занял 59 с)

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
| Строк в источниках | 146 |
| Разобрано в конфиги | 139 |
| Уникальных | 139 |
| Endpoint отвечает по TCP | 136 |
| YouTube доступен | 116 |
| + Telegram (HTTP) доступен | 112 |
| + дата-центр Telegram доступен | 112 |
| + скорость ≥ 2.0 Мбит/с | 88 |
| **В итоговом списке** | **88** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 48 |
| vless | 37 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 18 |
| KR | 14 |
| SG | 14 |
| DE | 8 |
| NL | 6 |
| FR | 5 |
| FI | 5 |
| PL | 5 |
| US | 3 |
| IE | 2 |
| SE | 2 |
| CA | 1 |
| EE | 1 |
| LV | 1 |
| GB | 1 |
| TR | 1 |
| TW | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 25.34 | 82 | 360 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 23.04 | 186 | 493 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 17.71 | 138 | 586 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.78 | 255 | 1789 |
| 5 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 12.78 | 270 | 298 |
| 6 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 12.57 | 254 | 1769 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.46 | 240 | 270 |
| 8 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 11.74 | 281 | 378 |
| 9 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 11.59 | 197 | 302 |
| 10 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 11.58 | 238 | 272 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
