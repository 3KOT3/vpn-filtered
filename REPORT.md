# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T06:18:47Z** UTC (прогон занял 58 с)

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
| Endpoint отвечает по TCP | 134 |
| YouTube доступен | 104 |
| + Telegram (HTTP) доступен | 94 |
| + дата-центр Telegram доступен | 94 |
| + скорость ≥ 3.0 Мбит/с | 49 |
| **В итоговом списке** | **49** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 38 |
| vmess | 7 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 7 |
| PH | 7 |
| JP | 6 |
| US | 4 |
| FI | 4 |
| HK | 3 |
| NL | 2 |
| PL | 2 |
| EE | 2 |
| SE | 2 |
| AT | 1 |
| IT | 1 |
| LT | 1 |
| ID | 1 |
| KR | 1 |
| TR | 1 |
| MD | 1 |
| IN | 1 |
| MY | 1 |
| AU | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 36.81 | 71 | 601 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 22.85 | 121 | 428 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 22.44 | 43 | 502 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.03 | 204 | 513 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 12.36 | 239 | 964 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 10.81 | 230 | 958 |
| 7 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 10.01 | 364 | 432 |
| 8 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.67 | 316 | 320 |
| 9 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 9.61 | 326 | 403 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.45 | 345 | 395 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
