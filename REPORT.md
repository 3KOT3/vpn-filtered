# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T03:12:10Z** UTC (прогон занял 36 с)

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
| Endpoint отвечает по TCP | 125 |
| YouTube доступен | 94 |
| + Telegram (HTTP) доступен | 90 |
| + дата-центр Telegram доступен | 90 |
| + скорость ≥ 3.0 Мбит/с | 58 |
| **В итоговом списке** | **58** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 48 |
| vmess | 6 |
| shadowsocks | 3 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| PH | 7 |
| US | 6 |
| PL | 5 |
| FI | 5 |
| JP | 5 |
| DE | 4 |
| NL | 4 |
| ?? | 3 |
| SG | 2 |
| TR | 2 |
| SE | 2 |
| IN | 2 |
| BR | 2 |
| CA | 1 |
| AT | 1 |
| IT | 1 |
| LT | 1 |
| HK | 1 |
| EE | 1 |
| HU | 1 |
| MD | 1 |
| KH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 47.63 | 36 | 359 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 29.09 | 37 | 255 |
| 3 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 28.80 | 53 | 331 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 17.61 | 187 | 713 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.32 | 120 | 530 |
| 6 | 🇸🇬[openproxylist.com] vless-SG | vless | SG | 15.36 | 517 | 1183 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.42 | 192 | 221 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 14.26 | 244 | 294 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.16 | 188 | 201 |
| 10 | 🏳[openproxylist.com] vmess- | vmess | ?? | 14.00 | 568 | 218 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
