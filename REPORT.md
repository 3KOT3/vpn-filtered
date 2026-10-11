# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-11T21:09:46Z** UTC (прогон занял 116 с)

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
| Строк в источниках | 146 |
| Разобрано в конфиги | 139 |
| Уникальных | 139 |
| Endpoint отвечает по TCP | 133 |
| YouTube доступен | 105 |
| + Telegram (HTTP) доступен | 99 |
| + дата-центр Telegram доступен | 99 |
| + скорость ≥ 2.0 Мбит/с | 76 |
| **В итоговом списке** | **76** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 36 |
| vless | 35 |
| shadowsocks | 4 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 14 |
| SG | 13 |
| KR | 8 |
| NL | 7 |
| DE | 7 |
| US | 6 |
| PL | 5 |
| FR | 3 |
| IE | 3 |
| SE | 2 |
| EE | 1 |
| ?? | 1 |
| FI | 1 |
| GB | 1 |
| LV | 1 |
| ID | 1 |
| TR | 1 |
| TW | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.84 | 126 | 417 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 17.84 | 212 | 400 |
| 3 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 17.33 | 161 | 486 |
| 4 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 12.31 | 222 | 882 |
| 5 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 12.19 | 226 | 907 |
| 6 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 12.05 | 226 | 902 |
| 7 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 12.01 | 228 | 888 |
| 8 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 11.95 | 224 | 1201 |
| 9 | 🇯🇵[openproxylist.com] trojan-JP | trojan | JP | 11.88 | 225 | 1196 |
| 10 | 🇯🇵[openproxylist.com] ss-JP | shadowsocks | JP | 11.85 | 357 | 1108 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
