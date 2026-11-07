# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-07T03:48:45Z** UTC (прогон занял 43 с)

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
| Строк в источниках | 444 |
| Разобрано в конфиги | 433 |
| Уникальных | 433 |
| Endpoint отвечает по TCP | 423 |
| YouTube доступен | 293 |
| + Telegram (HTTP) доступен | 250 |
| + дата-центр Telegram доступен | 250 |
| + скорость ≥ 3.0 Мбит/с | 143 |
| **В итоговом списке** | **143** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| shadowsocks | 50 |
| vless | 50 |
| vmess | 32 |
| trojan | 11 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 71 |
| CA | 16 |
| DE | 14 |
| FR | 7 |
| NL | 7 |
| GB | 5 |
| SE | 5 |
| ES | 4 |
| ?? | 3 |
| PL | 3 |
| CH | 3 |
| SG | 1 |
| AT | 1 |
| UA | 1 |
| IT | 1 |
| GE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 16.33 | 64 | 279 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 14.80 | 72 | 364 |
| 3 | 🇨🇦[openproxylist.com] trojan-CA | trojan | CA | 14.44 | 53 | 303 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.43 | 66 | 326 |
| 5 | [🇺🇸] [vm-no-ra] [261106-232032.528] | vmess | US | 14.41 | 77 | 284 |
| 6 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 13.25 | 71 | 367 |
| 7 | [🇨🇦] [vm-no-ra] [261106-232050.321] | vmess | CA | 12.10 | 81 | 328 |
| 8 | 🇨🇦[openproxylist.com] trojan-CA | trojan | CA | 11.99 | 53 | 296 |
| 9 | [🇨🇦] [vm-no-ra] [261106-232124.114] | vmess | CA | 11.76 | 84 | 304 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 11.67 | 75 | 381 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
