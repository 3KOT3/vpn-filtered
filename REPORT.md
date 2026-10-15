# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-15T02:02:10Z** UTC (прогон занял 55 с)

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
| Разобрано в конфиги | 141 |
| Уникальных | 141 |
| Endpoint отвечает по TCP | 130 |
| YouTube доступен | 106 |
| + Telegram (HTTP) доступен | 104 |
| + дата-центр Telegram доступен | 104 |
| + скорость ≥ 2.0 Мбит/с | 54 |
| **В итоговом списке** | **54** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 41 |
| trojan | 6 |
| vmess | 4 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| NL | 7 |
| US | 5 |
| DE | 5 |
| PL | 5 |
| HK | 5 |
| FI | 5 |
| SG | 5 |
| ?? | 4 |
| SE | 2 |
| TR | 2 |
| TH | 2 |
| KR | 2 |
| IT | 1 |
| ES | 1 |
| AT | 1 |
| AE | 1 |
| JP | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 29.07 | 34 | 272 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 27.66 | 80 | 328 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 26.03 | 107 | 342 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.04 | 182 | 684 |
| 5 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 15.26 | 217 | 239 |
| 6 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 15.22 | 197 | 212 |
| 7 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.92 | 194 | 186 |
| 8 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 14.67 | 197 | 194 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.42 | 194 | 227 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 14.31 | 223 | 291 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
