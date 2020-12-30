#  from flask import Flask
import requests
import json

from time import sleep

print("-------------------------------------------- Написание кода для бота в Telegram. Писать/Читать")

token = "1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs"
URL = "https://api.telegram.org/bot1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs/"


# Получает и возвращает все сообщения бота в JSON
def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


# Получает последнее сообщение
def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']
    result = {'chat_id': chat_id, 'text': text}
    return result


def write_json(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# 1. Тут мы получили информацию о боте и записали ее в файл "getMe.json"
r = requests.get(URL + 'getMe')
write_json(data=r.json(), file_name='getMe.json')

# 2. Записываем все сообщения в файл "messages.json"
result_get_updates = get_updates()
write_json(data=result_get_updates, file_name="messages.json")

# 3. Получаем последнее сообщение и записываем его в "last_message.json"
result_get_message = get_message()
write_json(data=result_get_message, file_name="last_message.json")
