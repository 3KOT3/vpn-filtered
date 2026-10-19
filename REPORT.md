# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-19T07:36:10Z** UTC (прогон занял 37 с)

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
| Строк в источниках | 144 |
| Разобрано в конфиги | 27 |
| Уникальных | 27 |
| Endpoint отвечает по TCP | 26 |
| YouTube доступен | 18 |
| + Telegram (HTTP) доступен | 16 |
| + дата-центр Telegram доступен | 16 |
| + скорость ≥ 3.0 Мбит/с | 11 |
| **В итоговом списке** | **11** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 10 |
| shadowsocks | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 7 |
| PH | 2 |
| CZ | 1 |
| HU | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.84 | 246 | 971 |
| 2 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.67 | 231 | 975 |
| 3 | 🇵🇭[openproxylist.com] vless-PH | vless | PH | 9.63 | 231 | 968 |
| 4 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 9.16 | 232 | 983 |
| 5 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 8.87 | 240 | 971 |
| 6 | 🇨🇿[openproxylist.com] ss-CZ | shadowsocks | CZ | 8.03 | 535 | 722 |
| 7 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.74 | 385 | 1058 |
| 8 | 🇭🇺[openproxylist.com] vless-HU | vless | HU | 7.45 | 356 | 373 |
| 9 | 🇵🇭[openproxylist.com] vless-PH | vless | PH | 7.36 | 388 | 1069 |
| 10 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 6.01 | 325 | 1138 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 86 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
