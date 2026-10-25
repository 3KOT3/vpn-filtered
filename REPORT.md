# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-25T02:24:23Z** UTC (прогон занял 52 с)

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
| Строк в источниках | 415 |
| Разобрано в конфиги | 393 |
| Уникальных | 393 |
| Endpoint отвечает по TCP | 390 |
| YouTube доступен | 288 |
| + Telegram (HTTP) доступен | 263 |
| + дата-центр Telegram доступен | 263 |
| + скорость ≥ 3.0 Мбит/с | 33 |
| **В итоговом списке** | **33** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| vless | 20 |
| vmess | 10 |
| shadowsocks | 2 |
| trojan | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| US | 16 |
| CA | 16 |
| SG | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇸🇬[openproxylist.com] vless-SG | vless | SG | 11.45 | 43 | 814 |
| 2 | [🇺🇸] [vl-re-ra] [261025-030634.006] | vless | US | 10.30 | 51 | 698 |
| 3 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 7.56 | 52 | 454 |
| 4 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 7.46 | 49 | 440 |
| 5 | [🇺🇸] [vl-re-ra] [261025-030607.423] | vless | US | 6.41 | 80 | 562 |
| 6 | 🇺🇸[openproxylist.com] vless-US | vless | US | 5.77 | 72 | 518 |
| 7 | [🇺🇸] [vl-re-ra] [261025-030943.653] | vless | US | 5.03 | 289 | 457 |
| 8 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 5.00 | 152 | 393 |
| 9 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 4.81 | 65 | 472 |
| 10 | 🇺🇸[openproxylist.com] vmess-US | vmess | US | 4.68 | 203 | 490 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| transport-xhttp-unsupported | 8 |
| vmess-http-obfs | 3 |
| vmess-header-type | 2 |
| ss-method-chacha20-poly1305 | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
