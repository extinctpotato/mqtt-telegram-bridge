#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import configparser as c
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Bridge:
    def __telegram_start(update, context):
        print("TEST!!!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hey!")
    def __init__(self, path):
        ini = c.ConfigParser()
        ini.read(path)
        self.upd = Updater(token=ini['TELEGRAM']['token'], use_context=True)
        dispatcher = self.upd.dispatcher
        tstart_handler = CommandHandler('start', self.__telegram_start)
        dispatcher.add_handler(tstart_handler)

if __name__ == '__main__':
    print("Starting")
    br = Bridge("config.ini")
    br.upd.start_polling()

