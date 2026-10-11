# Отфильтрованный список VPN-конфигов

Обновлено: **2026-10-11T14:24:36Z** UTC (прогон занял 54 с)

## Что проверялось

1. Endpoint принимает TCP-соединение.
2. Через прокси открывается `https://www.youtube.com/generate_204` (ждём HTTP 204).
3. Через прокси открывается `https://core.telegram.org/` (ждём HTTP 200).
4. Скорость туннеля к Google CDN не ниже **2.0 Мбит/с** (скачиваем 3072 КБ за не более 12 с).

## Воронка

| Шаг | Осталось |
| --- | ---: |
| Строк в источниках | 128 |
| Разобрано в конфиги | 124 |
| Уникальных | 124 |
| Endpoint отвечает по TCP | 121 |
| YouTube доступен | 89 |
| Telegram доступен | 77 |
| Скорость ≥ 2.0 Мбит/с | 54 |
| **В итоговом списке** | **54** |

## По протоколам

| Протокол | В списке |
| --- | ---: |
| trojan | 27 |
| vless | 22 |
| shadowsocks | 4 |
| vmess | 1 |

## По странам

| Страна | В списке |
| --- | ---: |
| JP | 14 |
| DE | 7 |
| KR | 7 |
| US | 5 |
| SG | 5 |
| NL | 3 |
| GB | 2 |
| IE | 2 |
| PL | 2 |
| SE | 1 |
| FR | 1 |
| LV | 1 |
| TR | 1 |
| ?? | 1 |
| TW | 1 |
| FI | 1 |

## Самые быстрые

| # | Имя | Протокол | Страна | Мбит/с | YouTube, мс | Telegram, мс |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 36.13 | 4157 | 1468 |
| 2 | 🇺🇸[openproxylist.com] ss-US | shadowsocks | US | 28.54 | 73 | 307 |
| 3 | 🇺🇸[openproxylist.com] trojan-US | trojan | US | 16.79 | 170 | 648 |
| 4 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 13.66 | 230 | 265 |
| 5 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 13.48 | 239 | 238 |
| 6 | 🇳🇱[openproxylist.com] vless-NL | vless | NL | 12.84 | 221 | 219 |
| 7 | 🇸🇪[openproxylist.com] vless-SE | vless | SE | 12.68 | 346 | 421 |
| 8 | 🇫🇷[openproxylist.com] vless-FR | vless | FR | 12.31 | 234 | 269 |
| 9 | 🇩🇪[openproxylist.com] vless-DE | vless | DE | 12.23 | 275 | 296 |
| 10 | 🇺🇸[openproxylist.com] vless-US | vless | US | 12.08 | 574 | 400 |

## Что не удалось проверить

| Причина | Конфигов |
| --- | ---: |
| vmess-http-obfs | 3 |
| vmess-header-type | 1 |

## Ссылки

- Обычный список: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1.txt
- Base64-подписка: https://github.com/3KOT3/vpn-filtered/raw/refs/heads/main/1-base64.txt
