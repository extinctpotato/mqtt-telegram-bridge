#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import configparser as c
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Bridge(mqtt.Client):
    def on_connect(self, mqtcc, obj, flags, rc):
        logging.info("Connected with result code {}".format(rc))

    def on_message(self, mqttc, obj, msg):
        notif = msg.payload
        notif = notif.decode("utf-8")
        logging.info("Received a message, forwarding")
        self.upd.bot.send_message(chat_id=int(self.ini['TELEGRAM']['chat_id']), text=notif)

    def __init__(self, config, telegram):
        mqtt.Client.__init__(self)
        self.ini = config
        self.connect(self.ini['MQTT']['host'],
                int(self.ini['MQTT']['port']),
                int(self.ini['MQTT']['timeout']))
        self.subscribe(self.ini['MQTT']['subscribe'])
        self.upd = telegram


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info("Initializing...")
    ini = c.ConfigParser()

    if len(sys.argv) != 2 or not ini.read(sys.argv[1]):
        logging.error("Invalid config, bailing out!")
        sys.exit(0)

    tel = Updater(ini['TELEGRAM']['token'], use_context=True)
    tel.start_polling()
    logging.info("Started Telegram Updater")

    br = Bridge(ini, tel)
    br.loop_start()
    logging.info("Started MQTT client")

    tel.idle()

if __name__ == '__main__':
    main()
