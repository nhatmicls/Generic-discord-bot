import typing
import os
import random

import pif_discord_bot

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
JSON_DIRECTORY = os.getenv("JSON_DIRECTORY")

if __name__ == "__main__":
    pif_discord_bot.update_config(TOKEN, DISCORD_GUILD, JSON_DIRECTORY)
    pif_discord_bot._exec()
