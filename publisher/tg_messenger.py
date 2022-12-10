from abc import ABC, abstractmethod

import telegram
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters


class BaseMessenger(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

    @abstractmethod
    def get_user_id(self, update: Update):
        pass

    @abstractmethod
    def start_bot(self, callback_action):
        pass


class TGMessenger(BaseMessenger):
    def __init__(self, token: str):
        self.updater, self.bot = None, None
        self.token = token

    def get_user_id(self, update: Update):
        try:
            user_id = update.message.chat.id
        except Exception:
            user_id = update.callback_query.message.chat.id
        return user_id

    def send_message(self, recipient:str, message:str):
        self.bot.send_message(recipient, message)

    def start_bot(self, callback_action):
        updater = Updater(self.token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, callback_action))
        updater.start_polling()
        bot = telegram.bot.Bot(self.token)
        self.updater = updater
        self.bot = bot





