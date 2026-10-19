# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-19T00:05:04Z** UTC (прогон занял 32 с)

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
| Строк в источниках | 146 |
| Разобрано в конфиги | 138 |
| Уникальных | 138 |
| Endpoint отвечает по TCP | 134 |
| YouTube доступен | 103 |
| + Telegram (HTTP) доступен | 98 |
| + дата-центр Telegram доступен | 98 |
| + скорость ≥ 3.0 Мбит/с | 49 |
| **В итоговом списке** | **49** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 41 |
| vmess | 5 |
| shadowsocks | 3 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 7 |
| DE | 7 |
| FI | 5 |
| PL | 4 |
| US | 3 |
| NL | 3 |
| SE | 2 |
| SG | 2 |
| IN | 2 |
| CA | 1 |
| UA | 1 |
| IT | 1 |
| HK | 1 |
| BR | 1 |
| GB | 1 |
| AT | 1 |
| KR | 1 |
| TR | 1 |
| LV | 1 |
| ID | 1 |
| EE | 1 |
| FR | 1 |
| MD | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] vless-US | vless | US | 14.20 | 102 | 595 |
| 2 | 🇺🇸[openproxylist.com] vless-US | vless | US | 13.68 | 136 | 381 |
| 3 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 13.05 | 164 | 448 |
| 4 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.59 | 153 | 395 |
| 5 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 8.33 | 297 | 351 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.27 | 241 | 966 |
| 7 | 🇺🇦[openproxylist.com] vless-UA | vless | UA | 8.09 | 328 | 342 |
| 8 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.91 | 232 | 1015 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 7.68 | 277 | 303 |
| 10 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.60 | 324 | 981 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-header-type | 4 |
| vmess-http-obfs | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
