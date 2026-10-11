# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-11T14:33:11Z** UTC (прогон занял 62 с)

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
| Строк в источниках | 128 |
| Разобрано в конфиги | 124 |
| Уникальных | 124 |
| Endpoint отвечает по TCP | 123 |
| YouTube доступен | 91 |
| + Telegram (HTTP) доступен | 87 |
| + дата-центр Telegram доступен | 87 |
| + скорость ≥ 2.0 Мбит/с | 62 |
| **В итоговом списке** | **62** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 28 |
| vless | 28 |
| shadowsocks | 5 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 15 |
| KR | 8 |
| US | 6 |
| DE | 6 |
| PL | 6 |
| SG | 5 |
| FR | 3 |
| NL | 3 |
| IE | 2 |
| FI | 2 |
| SE | 1 |
| LV | 1 |
| GB | 1 |
| TR | 1 |
| TH | 1 |
| ?? | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 30.95 | 74 | 4518 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 26.81 | 91 | 329 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 19.03 | 151 | 592 |
| 4 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 13.10 | 263 | 268 |
| 5 | 🇯🇵[openproxylist.com] ss-JP | shadowsocks | JP | 12.53 | 486 | 1215 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.29 | 135 | 620 |
| 7 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.27 | 234 | 231 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 11.81 | 259 | 282 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 11.46 | 3089 | 247 |
| 10 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 11.31 | 275 | 429 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
