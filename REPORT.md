# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T04:39:16Z** UTC (прогон занял 37 с)

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
| Строк в источниках | 149 |
| Разобрано в конфиги | 130 |
| Уникальных | 130 |
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 92 |
| + Telegram (HTTP) доступен | 86 |
| + дата-центр Telegram доступен | 86 |
| + скорость ≥ 3.0 Мбит/с | 58 |
| **В итоговом списке** | **58** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 46 |
| vmess | 7 |
| trojan | 3 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 7 |
| US | 6 |
| PH | 6 |
| DE | 5 |
| PL | 5 |
| FI | 5 |
| NL | 3 |
| KR | 3 |
| SG | 2 |
| ?? | 2 |
| TR | 2 |
| BR | 2 |
| IN | 2 |
| CA | 1 |
| IT | 1 |
| AT | 1 |
| HK | 1 |
| LT | 1 |
| EE | 1 |
| MD | 1 |
| ID | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 38.97 | 47 | 353 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 27.43 | 68 | 334 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 20.72 | 272 | 706 |
| 4 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 20.51 | 116 | 550 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 20.07 | 149 | 658 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.92 | 98 | 500 |
| 7 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 14.59 | 259 | 295 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.21 | 229 | 247 |
| 9 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.05 | 299 | 530 |
| 10 | 🇸🇬[openproxylist.com] vless-SG | vless | SG | 13.17 | 494 | 1079 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
