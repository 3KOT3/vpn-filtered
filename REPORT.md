# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-14T02:21:29Z** UTC (прогон занял 51 с)

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
| Строк в источниках | 149 |
| Разобрано в конфиги | 143 |
| Уникальных | 143 |
| Endpoint отвечает по TCP | 141 |
| YouTube доступен | 115 |
| + Telegram (HTTP) доступен | 106 |
| + дата-центр Telegram доступен | 106 |
| + скорость ≥ 2.0 Мбит/с | 54 |
| **В итоговом списке** | **54** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 35 |
| trojan | 14 |
| vmess | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 8 |
| US | 5 |
| NL | 5 |
| SG | 5 |
| FI | 4 |
| DE | 4 |
| PL | 3 |
| TR | 3 |
| ?? | 3 |
| EE | 2 |
| IE | 2 |
| HK | 2 |
| CA | 1 |
| UA | 1 |
| AT | 1 |
| SE | 1 |
| GB | 1 |
| ID | 1 |
| KR | 1 |
| LV | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 21.71 | 88 | 393 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.00 | 121 | 600 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 16.01 | 553 | 735 |
| 4 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 14.14 | 202 | 440 |
| 5 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.13 | 284 | 290 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 11.95 | 228 | 930 |
| 7 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.83 | 747 | 660 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 11.16 | 280 | 284 |
| 9 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.58 | 310 | 414 |
| 10 | 🇪🇪[openproxylist.com] vless-EE | vless | EE | 9.36 | 354 | 424 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
