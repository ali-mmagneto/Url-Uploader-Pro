
import logging
import logging.config
from pyrogram import enums

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from logging import getLogger, FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info, warning as log_warning

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[FileHandler('log.txt'), StreamHandler()],
                    level=INFO)

LOGGER = getLogger(__name__)

import os
import pytz
import datetime
from config import Config

from Uploader.database.database import Database

from pyrogram import Client


userbot = Client(name='userbot', api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.STRING_SESSION, parse_mode=enums.ParseMode.HTML, no_updates=True)
userbot.start() 

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="Uploader")
    Warrior = Client("@UPLOADER_X_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,

    plugins=plugins)
    Warrior.db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
    Warrior.broadcast_ids = {}
    Warrior.run()
