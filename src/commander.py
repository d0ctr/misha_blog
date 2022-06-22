import os
import logging
from typing import Dict
from functools import wraps

from telegram.ext.updater import Updater
from telegram import Update, Chat
from telegram.ext import  CommandHandler, CallbackContext

from .base_string import BaseString
from .shared import HandyDict

def dispatch_context(func):
    @wraps(func)
    def decorated_handler(cls, update: Update, context: CallbackContext):
        global items 
        items = HandyDict()

        items.bot = context.bot.name
        items.bot_id = context.bot.id

        items.user = update.effective_user.name
        items.user_id = update.effective_user.id

        if update.effective_chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
            items.chat = update.effective_chat.title
            items.chat_id = update.effective_chat.id
        elif update.effective_chat.type == Chat.CHANNEL:
            items.channel = update.effective_chat.title
            items.channel_id = update.effective_chat.id
        else:
            items.private_chat = update.effective_chat.title
            items.private_chat_id = update.effective_chat.id

        items.command = update.message.text

        return func(cls, update, context)

    return decorated_handler 


class Commander:
    def __init__(self, parentLogger: logging.Logger, updater: Updater):
        self.__updater = updater
        self.logger = parentLogger.getChild('commander')

        # adding commands handler
        self.__updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.__updater.dispatcher.add_handler(CommandHandler('help', self.help))
    
    @dispatch_context
    def start(self, update: Update, context: CallbackContext) -> None:
        self.logger.info(f'Received: {items}')
        update.message.reply_text(BaseString.start_message(items))

    @dispatch_context
    def help(self, update: Update, context: CallbackContext) -> None:
        self.logger.info(f'Received: {items}')
        update.message.reply_text(BaseString.help_message(items)) 
