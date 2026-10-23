# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-23T16:09:38Z** UTC (прогон занял 58 с)

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
| Строк в источниках | 379 |
| Разобрано в конфиги | 349 |
| Уникальных | 349 |
| Endpoint отвечает по TCP | 309 |
| YouTube доступен | 163 |
| + Telegram (HTTP) доступен | 123 |
| + дата-центр Telegram доступен | 123 |
| + скорость ≥ 3.0 Мбит/с | 48 |
| **В итоговом списке** | **48** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vmess | 19 |
| vless | 18 |
| shadowsocks | 9 |
| trojan | 2 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 20 |
| CA | 16 |
| ?? | 6 |
| GB | 4 |
| NL | 1 |
| DE | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 7.08 | 81 | 504 |
| 2 | 🏳[openproxylist.com] trojan- | trojan | ?? | 6.48 | 108 | 530 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 6.35 | 103 | 523 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 5.95 | 144 | 585 |
| 5 | [🇺🇸] [vl-re-ra] [261023-153447.744] | vless | US | 5.86 | 170 | 732 |
| 6 | [🇺🇸] [vm-no-ra] [261023-153806.365] | vmess | US | 5.69 | 123 | 338 |
| 7 | [🇺🇸] [vl-re-ra] [261023-153256.088] | vless | US | 5.55 | 82 | 324 |
| 8 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 5.53 | 105 | 561 |
| 9 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 4.93 | 130 | 573 |
| 10 | 🏳[openproxylist.com] ss- | shadowsocks | ?? | 4.84 | 129 | 323 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 17 |
| vmess-http-obfs | 3 |
| vmess-header-type | 3 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
