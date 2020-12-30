#  from flask import Flask
import requests

from time import sleep

print("-------------------------------------------- Написание кода для бота в Telegram. Писать/Читать")

token = "1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs"
URL = "https://api.telegram.org/bot1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs/"


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    print(r.content)


def main():
    r = requests.get(URL + 'getMe')
    print(r.json())
