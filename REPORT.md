# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-02T03:32:28Z** UTC (прогон занял 46 с)

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
| Строк в источниках | 440 |
| Разобрано в конфиги | 419 |
| Уникальных | 419 |
| Endpoint отвечает по TCP | 412 |
| YouTube доступен | 274 |
| + Telegram (HTTP) доступен | 260 |
| + дата-центр Telegram доступен | 260 |
| + скорость ≥ 3.0 Мбит/с | 136 |
| **В итоговом списке** | **136** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 61 |
| trojan | 49 |
| vmess | 26 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 57 |
| CA | 42 |
| GB | 13 |
| NL | 7 |
| DE | 4 |
| PL | 3 |
| ES | 3 |
| MX | 2 |
| UA | 1 |
| ?? | 1 |
| CL | 1 |
| CZ | 1 |
| CH | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 13.95 | 68 | 338 |
| 2 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 13.50 | 66 | 577 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 13.35 | 61 | 349 |
| 4 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.92 | 57 | 331 |
| 5 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.92 | 71 | 523 |
| 6 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.33 | 62 | 335 |
| 7 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 12.30 | 59 | 332 |
| 8 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 12.12 | 120 | 623 |
| 9 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 11.81 | 72 | 520 |
| 10 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 11.66 | 79 | 680 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 9 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
