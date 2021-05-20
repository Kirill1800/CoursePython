import requests
import telebot


class Bot:

    TOKEN = "1624243252:AAFQo5YHwdK7O2akLKZB-KyqOdTBfvBV6Zw"
    BOT = None

    def __init__(self):
        requests.get(url="https://api.telegram.org/bot{}/setWebhook?url=".format(token))
        self.BOT = telebot.TeleBot(token=self.TOKEN)
        self.BOT.send_message(221824550, "Перезапуск!")