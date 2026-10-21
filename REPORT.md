# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-21T02:36:33Z** UTC (прогон занял 52 с)

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
| Строк в источниках | 502 |
| Разобрано в конфиги | 336 |
| Уникальных | 336 |
| Endpoint отвечает по TCP | 330 |
| YouTube доступен | 250 |
| + Telegram (HTTP) доступен | 237 |
| + дата-центр Telegram доступен | 237 |
| + скорость ≥ 3.0 Мбит/с | 2 |
| **В итоговом списке** | **5** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 4 |
| shadowsocks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 2 |
| NL | 2 |
| GB | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 3.62 | 75 | 338 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 3.22 | 139 | 628 |
| 3 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 2.38 | 246 | 256 |
| 4 | 🇬🇧[openproxylist.com] vless-GB | vless | GB | 2.34 | 598 | 282 |
| 5 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 2.34 | 253 | 257 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 5 |
| vmess-http-obfs | 3 |
| vmess-header-type | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
