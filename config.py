import logging
from pathlib import Path

import constants

SESSION_NAME = "account"

API_ID = 26087088
API_HASH = "0c649b615f94e6c8eca8de196249b734"

BOT_TOKENS = ["7286764077:AAFMqxpZqbAar-5Kqj7w7d7hfbf5oA_5ZQc"]

CHECK_INTERVAL = 60.0
CHECK_UPGRADES_PER_CYCLE = 2

DATA_FILEPATH = Path("/data/star_gifts.json")

DATA_SAVER_DELAY = 2.0
NOTIFY_CHAT_ID = -1002614267492
NOTIFY_UPGRADES_CHAT_ID = -1002751596218

NOTIFY_AFTER_STICKER_DELAY = 10.0
NOTIFY_AFTER_TEXT_DELAY = 10.0
TIMEZONE = "Europe/Warsaw"

CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.INFO
HTTP_REQUEST_TIMEOUT = 20.0

NOTIFY_TEXT = """\
{title}

№ {number} (<code>{id}</code>)
{total_amount}{available_amount}{sold_out}
💎 Price: {price} ⭐️
♻️ Convert price: {convert_price} ⭐️
"""

NOTIFY_TEXT_TITLES = {
    True: "🔥 A new limited gift has appeared",
    False: "❄️ A new gift has appeared"
}

NOTIFY_TEXT_TOTAL_AMOUNT = "\n🎯 Total amount: {total_amount}"
NOTIFY_TEXT_AVAILABLE_AMOUNT = "\n❓ Available amount: {available_amount} ({same_str}{available_percentage}%, updated at {updated_datetime} UTC)\n"
NOTIFY_TEXT_SOLD_OUT = "\n⏰ Completely sold out in {sold_out}\n"

NOTIFY_UPGRADES_TEXT = "Gift is upgradable! (<code>{id}</code>)"
