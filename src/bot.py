import os
import logging

from telegram.ext.updater import Updater

from .commander import Commander

def start(parentLogger: logging.Logger):
    logger = parentLogger.getChild('bot')
    # checking that neccessary is present
    if not os.getenv('BOT_TELEGRAM_API'): 
        logger.debug('Impossible to work without API token')
        exit()

    updater = Updater(os.getenv('BOT_TELEGRAM_API'), use_context=True)

    Commander(logger, updater)
    updater.start_polling()
