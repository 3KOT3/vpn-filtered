# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-13T22:02:15Z** UTC (прогон занял 54 с)

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
| Разобрано в конфиги | 139 |
| Уникальных | 139 |
| Endpoint отвечает по TCP | 129 |
| YouTube доступен | 101 |
| + Telegram (HTTP) доступен | 97 |
| + дата-центр Telegram доступен | 97 |
| + скорость ≥ 2.0 Мбит/с | 49 |
| **В итоговом списке** | **49** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 27 |
| trojan | 14 |
| shadowsocks | 4 |
| vmess | 4 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 10 |
| JP | 7 |
| NL | 4 |
| SG | 4 |
| FI | 3 |
| DE | 3 |
| IE | 2 |
| PL | 2 |
| KR | 2 |
| US | 1 |
| AT | 1 |
| UA | 1 |
| CA | 1 |
| EE | 1 |
| ID | 1 |
| GB | 1 |
| TH | 1 |
| RO | 1 |
| OM | 1 |
| TR | 1 |
| HK | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 25.07 | 89 | 383 |
| 2 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 12.80 | 235 | 954 |
| 3 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 11.75 | 528 | 904 |
| 4 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 10.75 | 276 | 421 |
| 5 | 🇦🇹[openproxylist.com] ss-AT | shadowsocks | AT | 10.54 | 355 | 442 |
| 6 | 🇫🇮[openproxylist.com] vless-FI | vless | FI | 10.18 | 349 | 457 |
| 7 | 🇮🇪[openproxylist.com] trojan-IE | trojan | IE | 9.96 | 398 | 315 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 9.82 | 342 | 398 |
| 9 | 🇮🇪[openproxylist.com] vless-IE | vless | IE | 9.68 | 353 | 381 |
| 10 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 9.67 | 294 | 341 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
