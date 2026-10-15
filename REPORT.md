# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-15T15:51:19Z** UTC (прогон занял 44 с)

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
| Разобрано в конфиги | 138 |
| Уникальных | 138 |
| Endpoint отвечает по TCP | 119 |
| YouTube доступен | 77 |
| + Telegram (HTTP) доступен | 69 |
| + дата-центр Telegram доступен | 69 |
| + скорость ≥ 2.0 Мбит/с | 39 |
| **В итоговом списке** | **39** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 31 |
| trojan | 4 |
| vmess | 2 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 12 |
| DE | 5 |
| US | 2 |
| HK | 2 |
| FI | 2 |
| NL | 2 |
| PL | 2 |
| SG | 2 |
| CA | 1 |
| AT | 1 |
| IT | 1 |
| UA | 1 |
| TR | 1 |
| SE | 1 |
| JP | 1 |
| KR | 1 |
| ES | 1 |
| TW | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 31.55 | 70 | 570 |
| 2 | 🏳[openproxylist.com] vless- | vless | ?? | 18.93 | 81 | 859 |
| 3 |  | vmess | ?? | 18.63 | 140 | 816 |
| 4 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 16.10 | 165 | 446 |
| 5 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 9.30 | 367 | 447 |
| 6 | 🇭🇰[openproxylist.com] vless-HK | vless | HK | 9.30 | 310 | 1175 |
| 7 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.26 | 348 | 380 |
| 8 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 9.18 | 359 | 443 |
| 9 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 9.06 | 347 | 315 |
| 10 | 🇮🇹[openproxylist.com] ss-IT | shadowsocks | IT | 8.93 | 352 | 412 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
