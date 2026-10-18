# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-18T20:26:33Z** UTC (прогон занял 28 с)

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
| Строк в источниках | 148 |
| Разобрано в конфиги | 35 |
| Уникальных | 35 |
| Endpoint отвечает по TCP | 32 |
| YouTube доступен | 22 |
| + Telegram (HTTP) доступен | 19 |
| + дата-центр Telegram доступен | 19 |
| + скорость ≥ 3.0 Мбит/с | 13 |
| **В итоговом списке** | **13** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 11 |
| shadowsocks | 1 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| ?? | 3 |
| DE | 2 |
| CA | 1 |
| NL | 1 |
| PL | 1 |
| JP | 1 |
| MD | 1 |
| BR | 1 |
| FI | 1 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇨🇦[openproxylist.com] vless-CA | vless | CA | 30.83 | 77 | 320 |
| 2 | 🇳🇱[openproxylist.com] ss-NL | shadowsocks | NL | 10.85 | 246 | 286 |
| 3 | 🇵🇱[openproxylist.com] vless-PL | vless | PL | 10.07 | 278 | 305 |
| 4 | 🏳[openproxylist.com] vless- | vless | ?? | 9.54 | 330 | 357 |
| 5 | 🇩🇪[openproxylist.com] vmess-DE | vmess | DE | 9.07 | 247 | 270 |
| 6 | 🇯🇵[openproxylist.com] vless-JP | vless | JP | 7.98 | 302 | 1038 |
| 7 | 🇲🇩[openproxylist.com] vless-MD | vless | MD | 7.94 | 406 | 420 |
| 8 | 🏳[openproxylist.com] vless- | vless | ?? | 6.90 | 396 | 538 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 6.19 | 298 | 313 |
| 10 | 🏳[openproxylist.com] vless- | vless | ?? | 6.01 | 328 | 1039 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| не ответил из России | 109 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
