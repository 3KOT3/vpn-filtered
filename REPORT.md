# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T06:06:34Z** UTC (прогон занял 50 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Через прокси открывается TCP-соединение с дата-центром Telegram (149.154.167.51, 149.154.175.53, 149.154.167.91: 443) — это отсекает прокси, чей IP заблокирован самим Telegram.
5. Скорость туннеля к Google CDN не ниже **3.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

В список попадают только те конфиги, которые прошли **все** шаги: и YouTube, и Telegram, и скорость.

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 147 |
| Разобрано в конфиги | 141 |
| Уникальных | 141 |
| Endpoint отвечает по TCP | 138 |
| YouTube доступен | 102 |
| + Telegram (HTTP) доступен | 94 |
| + дата-центр Telegram доступен | 94 |
| + скорость ≥ 3.0 Мбит/с | 52 |
| **В итоговом списке** | **52** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 41 |
| shadowsocks | 4 |
| vmess | 4 |
| trojan | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| DE | 6 |
| PH | 6 |
| US | 5 |
| JP | 5 |
| NL | 4 |
| HK | 4 |
| FI | 4 |
| KR | 3 |
| PL | 3 |
| SG | 2 |
| IT | 1 |
| EE | 1 |
| AT | 1 |
| LT | 1 |
| ID | 1 |
| SE | 1 |
| TR | 1 |
| MD | 1 |
| MY | 1 |
| IN | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 27.02 | 71 | 561 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 23.64 | 123 | 410 |
| 3 | 🇺🇸[openproxylist.com] vless-US | vless | US | 19.88 | 214 | 559 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 18.47 | 153 | 372 |
| 5 | 🇯🇵[openproxylist.com] ss-JP | shadowsocks | JP | 12.78 | 226 | 1188 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 11.73 | 232 | 981 |
| 7 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 11.70 | 233 | 965 |
| 8 | 🇰🇷[openproxylist.com] vmess-KR | vmess | KR | 9.71 | 430 | 1093 |
| 9 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 9.62 | 332 | 368 |
| 10 | 🇰🇷[openproxylist.com] trojan-KR | trojan | KR | 9.62 | 335 | 1040 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 2 |
| vmess-http-obfs | 2 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
