# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-16T16:43:00Z** UTC (прогон занял 58 с)

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
| Строк в источниках | 148 |
| Разобрано в конфиги | 133 |
| Уникальных | 133 |
| Endpoint отвечает по TCP | 118 |
| YouTube доступен | 88 |
| + Telegram (HTTP) доступен | 79 |
| + дата-центр Telegram доступен | 79 |
| + скорость ≥ 2.0 Мбит/с | 50 |
| **В итоговом списке** | **50** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 35 |
| trojan | 7 |
| vmess | 4 |
| shadowsocks | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 26 |
| BR | 5 |
| FI | 3 |
| DE | 2 |
| SG | 2 |
| JP | 2 |
| ES | 1 |
| IT | 1 |
| HK | 1 |
| TR | 1 |
| US | 1 |
| ZA | 1 |
| ID | 1 |
| IN | 1 |
| TW | 1 |
| UA | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] vless- | vless | ?? | 37.28 | 60 | 448 |
| 2 |  | vmess | ?? | 36.87 | 175 | 364 |
| 3 | 🇪🇸[openproxylist.com] vless-ES | vless | ES | 35.72 | 39 | 551 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 28.11 | 39 | 341 |
| 5 | 🏳[openproxylist.com] vless- | vless | ?? | 15.52 | 186 | 692 |
| 6 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 14.16 | 238 | 276 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.87 | 195 | 228 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 13.15 | 2648 | 238 |
| 9 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 12.53 | 279 | 310 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 12.20 | 231 | 283 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
