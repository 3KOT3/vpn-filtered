# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-17T23:46:00Z** UTC (прогон занял 36 с)

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
| Разобрано в конфиги | 125 |
| Уникальных | 125 |
| Endpoint отвечает по TCP | 122 |
| YouTube доступен | 99 |
| + Telegram (HTTP) доступен | 84 |
| + дата-центр Telegram доступен | 84 |
| + скорость ≥ 3.0 Мбит/с | 53 |
| **В итоговом списке** | **53** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 40 |
| shadowsocks | 5 |
| vmess | 5 |
| trojan | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 5 |
| DE | 5 |
| NL | 5 |
| FI | 5 |
| PL | 4 |
| JP | 4 |
| ?? | 3 |
| SG | 3 |
| TR | 2 |
| IN | 2 |
| KR | 2 |
| CA | 1 |
| AT | 1 |
| IT | 1 |
| HK | 1 |
| SE | 1 |
| HU | 1 |
| LT | 1 |
| RU | 1 |
| MD | 1 |
| BR | 1 |
| KH | 1 |
| ID | 1 |
| TH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 35.49 | 37 | 342 |
| 2 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 31.89 | 67 | 324 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 30.41 | 68 | 270 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 20.67 | 116 | 523 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 16.51 | 198 | 238 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.75 | 184 | 709 |
| 7 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 14.35 | 247 | 323 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.24 | 184 | 193 |
| 9 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 14.22 | 214 | 249 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 13.56 | 251 | 308 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
