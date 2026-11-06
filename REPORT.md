# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-06T13:29:17Z** UTC (прогон занял 50 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 512 КБ за не более 15 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 428 |
| Разобрано в конфиги | 412 |
| Уникальных | 412 |
| Endpoint отвечает по TCP | 382 |
| YouTube доступен | 197 |
| + Telegram (HTTP) доступен | 181 |
| + дата-центр Telegram доступен | 181 |
| + скорость ≥ 3.0 Мбит/с | 88 |
| **В итоговом списке** | **88** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 42 |
| vmess | 31 |
| shadowsocks | 14 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 50 |
| ?? | 10 |
| CA | 9 |
| DE | 7 |
| NL | 4 |
| GB | 2 |
| FR | 1 |
| AT | 1 |
| ES | 1 |
| FI | 1 |
| SE | 1 |
| PL | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 11.94 | 70 | 408 |
| 2 | 🇺🇸 United States, North Bergen | [BL] | vless | US | 9.13 | 457 | 405 |
| 3 | 🇺🇸 United States, North Bergen | [BL] | vless | US | 8.35 | 166 | 414 |
| 4 | 🇺🇸 United States, North Bergen | [BL] | vless | US | 7.77 | 284 | 409 |
| 5 | 🇺🇸 United States, North Bergen | [BL] | vless | US | 7.75 | 286 | 398 |
| 6 | [🇺🇸] [vm-no-ra] [261106-052557.711] | vmess | US | 7.35 | 110 | 332 |
| 7 | [🇨🇦] [vm-no-ra] [261106-052614.510] | vmess | CA | 7.13 | 114 | 368 |
| 8 | 🏳[openproxylist.com] vmess- | vmess | ?? | 7.04 | 148 | 430 |
| 9 | [🇺🇸] [vm-no-ra] [261106-052623.519] | vmess | US | 6.84 | 108 | 526 |
| 10 | 🇺🇸 United States, North Bergen | [BL] | vless | US | 6.81 | 448 | 414 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
