# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-23T10:44:36Z** UTC (прогон занял 36 с)

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
| Строк в источниках | 357 |
| Разобрано в конфиги | 337 |
| Уникальных | 337 |
| Endpoint отвечает по TCP | 322 |
| YouTube доступен | 187 |
| + Telegram (HTTP) доступен | 171 |
| + дата-центр Telegram доступен | 171 |
| + скорость ≥ 3.0 Мбит/с | 11 |
| **В итоговом списке** | **11** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 9 |
| shadowsocks | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| CA | 7 |
| GB | 2 |
| SG | 1 |
| US | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 5.93 | 72 | 754 |
| 2 | 🌐 Anycast-IP | 🇬🇧 🇷🇺 | [BL] | vless | GB | 5.83 | 91 | 785 |
| 3 | 🇨🇦[openproxylist.com] ss-CA | shadowsocks | CA | 5.13 | 1078 | 657 |
| 4 | 🇸🇬[openproxylist.com] vless-SG | vless | SG | 4.28 | 97 | 674 |
| 5 | 🇺🇸[openproxylist.com] vless-US | vless | US | 4.19 | 151 | 572 |
| 6 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 3.51 | 94 | 704 |
| 7 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 3.24 | 89 | 702 |
| 8 | 🇨🇦[openproxylist.com] ss-CA | shadowsocks | CA | 3.20 | 1916 | 1709 |
| 9 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 3.17 | 92 | 747 |
| 10 | 🌐 Anycast-IP | 🇨🇦 🇬🇧 🇷🇺 | [BL] | vless | CA | 3.17 | 89 | 680 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 5 |
| vmess-http-obfs | 4 |
| vmess-header-type | 3 |
| ss-method-chacha20-poly1305 | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
