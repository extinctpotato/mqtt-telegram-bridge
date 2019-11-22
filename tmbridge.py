#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import configparser as c
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Bridge(mqtt.Client):
    def on_connect(self, mqtcc, obj, flags, rc):
        print("Connected with result code {}".format(rc))

    def on_message(self, mqttc, obj, msg):
        notif = msg.payload
        notif = notif.decode("utf-8")
        print("[{}] {}".format(msg.topic, notif))
        self.upd.bot.send_message(chat_id=870060908, text=notif)

    def __init__(self, config, telegram):
        mqtt.Client.__init__(self)
        self.ini = config
        '''self.connect(self.ini['MQTT']['host'],
                self.ini['MQTT']['port'],
                self.ini['MQTT']['timeout'])'''
        self.connect("localhost", 1883, 60)
        self.subscribe(self.ini['MQTT']['subscribe'])
        self.upd = telegram
        print("Aight")

if __name__ == '__main__':
    print("Starting")
    ini = c.ConfigParser()
    ini.read(sys.argv[1])
    tel = Updater(ini['TELEGRAM']['token'], use_context=True)
    tel.start_polling()
    br = Bridge(ini, tel)
    rc = 0
    while rc == 0:
        rc = br.loop()
