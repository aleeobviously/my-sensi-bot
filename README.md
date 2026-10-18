# Rynox Sensi AI — Telegram Sensitivity Bot

An open-source Telegram bot that generates mobile shooter sensitivity settings for players, based on their device's refresh rate.

**Live bot:** [@RynoxSensi_bot](https://t.me/RynoxSensi_bot)

## What it does

Players open the bot, pick a language, verify they have joined the community channel, choose their device refresh rate, and instantly receive a full sensitivity profile:

- **Lens tab** — camera sensitivity, ADS sensitivity, and free-look camera values
- **Gyroscope tab** — gyroscope sensitivity and ADS gyroscope values

Settings are calculated by scaling tested base values by the selected refresh rate (60 Hz ×1.0, 90 Hz ×1.1, 120 Hz+ ×1.2), so players on higher-refresh-rate devices get proportionally adjusted values instead of one-size-fits-all numbers copied from a screenshot.

## Features

- **4 languages** — full interface in English, Urdu, Hindi, and Arabic, selectable from an inline keyboard
- **Refresh-rate profiles** — dedicated 60 Hz, 90 Hz, and 120 Hz+ modes
- **Community channel verification** — checks membership of the @RynoxCheats Telegram channel before generating settings
- **Inline-keyboard flow** — /start, language, refresh rate, Lens/Gyroscope tabs, back navigation, and a share button; no commands to memorise
- **Lightweight** — a single Python file, in-memory user state, no database

## Tech stack

- Python
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) (`telebot`, threaded polling)

## Run it yourself

```bash
pip install -r requirements.txt
```

Set your own Telegram bot token (from [@BotFather](https://t.me/BotFather)) as an environment variable — never commit a token to source code:

```bash
export BOT_TOKEN="your-token-here"
python bot.py
```

## Project status

Early-stage open-source project by a solo maintainer, shared for the mobile gaming community — especially players in Pakistan, India, and the wider Urdu/Hindi/Arabic-speaking audience who rarely get gaming tools in their own language. Contributions, translations, and device-profile suggestions are welcome via issues and pull requests.

## Licence

MIT — see [LICENSE](LICENSE).
