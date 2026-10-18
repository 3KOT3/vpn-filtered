# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T15:40:05Z** UTC (прогон занял 284 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 2048 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 17777 |
| Разобрано в конфиги | 17164 |
| Уникальных | 17164 |
| Endpoint отвечает по TCP | 9116 |
| YouTube доступен | 1955 |
| + Telegram (HTTP) доступен | 1602 |
| + дата-центр Telegram доступен | 1602 |
| + скорость ≥ 3.0 Мбит/с | 958 |
| **В итоговом списке** | **958** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 831 |
| vmess | 75 |
| http | 18 |
| shadowsocks | 16 |
| hysteria2 | 10 |
| trojan | 7 |
| socks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| XX | 288 |
| US | 262 |
| NL | 101 |
| GB | 43 |
| CA | 38 |
| FR | 32 |
| DE | 19 |
| RU | 18 |
| SG | 16 |
| FI | 13 |
| JP | 13 |
| SE | 9 |
| AE | 8 |
| TR | 8 |
| PL | 7 |
| IT | 7 |
| ES | 7 |
| BY | 5 |
| UA | 5 |
| HK | 5 |
| TH | 5 |
| IN | 5 |
| LU | 5 |
| IQ | 4 |
| RO | 4 |
| BR | 4 |
| KR | 4 |
| CH | 3 |
| AT | 3 |
| IL | 2 |
| CZ | 2 |
| HU | 2 |
| ID | 2 |
| CO | 1 |
| EE | 1 |
| KZ | 1 |
| LT | 1 |
| LV | 1 |
| MD | 1 |
| EC | 1 |
| ZA | 1 |
| IE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | [OpenRay] 🌐XX-2742 | vless | XX | 32.90 | 55 | 610 |
| 2 | [OpenRay] 🌐XX-1696 | vless | XX | 31.98 | 40 | 626 |
| 3 | [OpenRay] 🌐XX-3524 | vless | XX | 31.47 | 39 | 619 |
| 4 | [OpenRay] 🇺🇸US-5347 | vless | US | 29.98 | 61 | 295 |
| 5 | [OpenRay] 🌐XX-1661 | vless | XX | 28.68 | 38 | 616 |
| 6 | [OpenRay] 🇺🇸US-5218 | vless | US | 28.44 | 89 | 349 |
| 7 | [OpenRay] 🌐XX-1421 | vless | XX | 27.36 | 41 | 636 |
| 8 | [OpenRay] 🌐XX-3139 | vless | XX | 27.10 | 35 | 591 |
| 9 | [OpenRay] 🇺🇸US-5229 | vmess | US | 27.06 | 66 | 308 |
| 10 | [OpenRay] 🇨🇦CA-271 | vless | CA | 26.81 | 45 | 787 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 301 |
| vless-encryption | 153 |
| vmess-header-type | 47 |
| transport-unknown | 25 |
| vmess-http-obfs | 22 |
| ss-method-chacha20-poly1305 | 5 |
| ss-bad-credentials | 2 |
| ss-missing-host | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
