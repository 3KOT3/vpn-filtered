# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-24T02:36:15Z** UTC (прогон занял 45 с)

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
| Строк в источниках | 436 |
| Разобрано в конфиги | 399 |
| Уникальных | 399 |
| Endpoint отвечает по TCP | 390 |
| YouTube доступен | 279 |
| + Telegram (HTTP) доступен | 256 |
| + дата-центр Telegram доступен | 256 |
| + скорость ≥ 3.0 Мбит/с | 36 |
| **В итоговом списке** | **36** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 21 |
| vmess | 5 |
| shadowsocks | 5 |
| trojan | 5 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 22 |
| CA | 13 |
| GB | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 9.41 | 69 | 517 |
| 2 | [🇺🇸] [vm-no-ra] [261024-011526.171] | vmess | US | 6.54 | 81 | 480 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 6.38 | 62 | 455 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 5.94 | 50 | 471 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 5.91 | 53 | 468 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 5.82 | 50 | 471 |
| 7 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 5.82 | 49 | 471 |
| 8 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 5.62 | 45 | 754 |
| 9 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 5.48 | 31 | 465 |
| 10 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 5.36 | 49 | 474 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 24 |
| vmess-http-obfs | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
