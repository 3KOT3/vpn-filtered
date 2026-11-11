# Отфильтрованный список VPN-конфигов

Обновлено: **2026-11-11T03:51:02Z** UTC (прогон занял 40 с)

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
| Строк в источниках | 447 |
| Разобрано в конфиги | 389 |
| Уникальных | 389 |
| Endpoint отвечает по TCP | 355 |
| YouTube доступен | 243 |
| + Telegram (HTTP) доступен | 223 |
| + дата-центр Telegram доступен | 223 |
| + скорость ≥ 3.0 Мбит/с | 100 |
| **В итоговом списке** | **100** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 54 |
| vless | 41 |
| shadowsocks | 5 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 75 |
| CA | 15 |
| DE | 3 |
| NL | 2 |
| IT | 2 |
| MX | 1 |
| TW | 1 |
| KR | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.93 | 33 | 458 |
| 2 | [🇺🇸] [vm-no-ra] [261111-050805.756] | vmess | US | 18.51 | 19 | 477 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 12.34 | 74 | 426 |
| 4 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 11.16 | 67 | 403 |
| 5 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 10.68 | 90 | 419 |
| 6 | [🇺🇸] [vm-no-ra] [261111-050750.128] | vmess | US | 10.64 | 112 | 634 |
| 7 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 10.63 | 92 | 401 |
| 8 | [🇺🇸] [vm-no-ra] [261111-050750.758] | vmess | US | 10.00 | 106 | 601 |
| 9 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 9.97 | 88 | 406 |
| 10 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 9.73 | 97 | 388 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 55 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
