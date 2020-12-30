#  from flask import Flask
import requests
import json

from time import sleep

print("-------------------------------------------- Написание кода для бота в Telegram. Писать/Читать")

token = "1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs"
URL = "https://api.telegram.org/bot1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs/"


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']
    print(text)
    #  result = {'chat_id': chat_id, 'text': text}
    #  return result


# def main():
#     d = get_updates()
#     get_message()
#
#     with open('updates.json', 'w') as file:
#         json.dump(d, file, indent=2, ensure_ascii=False)


def write_json(data, file_name='answer.json'):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    r = requests.get(URL + 'getMe')
    write_json(r.json())


if __name__ == '__main__':
    main()