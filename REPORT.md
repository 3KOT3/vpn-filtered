# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-15T10:27:33Z** UTC (прогон занял 57 с)

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
| Разобрано в конфиги | 125 |
| Уникальных | 125 |
| Endpoint отвечает по TCP | 117 |
| YouTube доступен | 81 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 2.0 Мбит/с | 43 |
| **В итоговом списке** | **43** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 28 |
| trojan | 7 |
| vmess | 5 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 6 |
| ?? | 6 |
| SG | 6 |
| HK | 4 |
| PL | 3 |
| US | 2 |
| NL | 2 |
| TR | 2 |
| KR | 2 |
| SE | 2 |
| TH | 2 |
| AT | 1 |
| IT | 1 |
| FI | 1 |
| IN | 1 |
| EE | 1 |
| JP | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 30.41 | 68 | 561 |
| 2 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 9.52 | 379 | 426 |
| 3 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 9.48 | 316 | 862 |
| 4 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 9.36 | 315 | 3689 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.18 | 387 | 379 |
| 6 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.14 | 341 | 405 |
| 7 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 8.89 | 349 | 439 |
| 8 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 8.67 | 343 | 434 |
| 9 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 8.66 | 342 | 433 |
| 10 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 8.60 | 405 | 485 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
