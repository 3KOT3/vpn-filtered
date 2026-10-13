# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-13T04:07:33Z** UTC (прогон занял 55 с)

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
| Endpoint отвечает по TCP | 143 |
| YouTube доступен | 113 |
| + Telegram (HTTP) доступен | 109 |
| + дата-центр Telegram доступен | 109 |
| + скорость ≥ 2.0 Мбит/с | 85 |
| **В итоговом списке** | **85** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 41 |
| vless | 38 |
| shadowsocks | 4 |
| vmess | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 18 |
| KR | 13 |
| DE | 8 |
| PL | 7 |
| US | 6 |
| NL | 4 |
| SG | 4 |
| IE | 3 |
| EE | 3 |
| FI | 3 |
| ?? | 3 |
| SE | 2 |
| FR | 1 |
| AT | 1 |
| LV | 1 |
| TR | 1 |
| TW | 1 |
| RO | 1 |
| ID | 1 |
| HK | 1 |
| AR | 1 |
| GB | 1 |
| TH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 26.77 | 75 | 609 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 22.85 | 161 | 528 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 21.35 | 165 | 473 |
| 4 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 19.77 | 175 | 410 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 13.71 | 227 | 939 |
| 6 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 13.35 | 222 | 900 |
| 7 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 13.22 | 228 | 867 |
| 8 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 11.07 | 264 | 344 |
| 9 | 🇰🇷[openproxylist.com] trojan-KR | trojan | KR | 11.02 | 332 | 943 |
| 10 | 🇰🇷[openproxylist.com] trojan-KR | trojan | KR | 10.74 | 332 | 957 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
