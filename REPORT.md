# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T05:37:33Z** UTC (прогон занял 50 с)

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
| Строк в источниках | 147 |
| Разобрано в конфиги | 141 |
| Уникальных | 141 |
| Endpoint отвечает по TCP | 138 |
| YouTube доступен | 107 |
| + Telegram (HTTP) доступен | 96 |
| + дата-центр Telegram доступен | 96 |
| + скорость ≥ 3.0 Мбит/с | 56 |
| **В итоговом списке** | **56** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 46 |
| trojan | 4 |
| shadowsocks | 3 |
| vmess | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 8 |
| PH | 7 |
| US | 5 |
| JP | 5 |
| NL | 4 |
| PL | 3 |
| FI | 3 |
| SG | 3 |
| HK | 3 |
| SE | 2 |
| IN | 2 |
| KR | 2 |
| AT | 1 |
| LT | 1 |
| EE | 1 |
| IT | 1 |
| TR | 1 |
| ID | 1 |
| KH | 1 |
| MY | 1 |
| MD | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 41.70 | 37 | 344 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 38.66 | 36 | 281 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 16.16 | 183 | 638 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.75 | 194 | 230 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.24 | 352 | 577 |
| 6 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 14.18 | 208 | 241 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.83 | 229 | 265 |
| 8 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 13.73 | 248 | 279 |
| 9 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 12.94 | 296 | 303 |
| 10 | 🇱🇹[openproxylist.com] vless-LT | vless | LT | 12.84 | 326 | 378 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
