from time import sleep

print("-------------------------------------------- Написание кода для бота в Telegram. Писать/Читать")

TOKEN = "1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs"
URL = "https://api.telegram.org/bot" + TOKEN + "/"


# Проверить работает ли бот (Ответ: Response [200])
def get_bot_check():
    import requests
    result = requests.get(URL + "getupdates")
    return result


# Обновить/Получить JSON
def get_updates():
    import requests
    result = requests.get(URL + "getupdates")
    return result.json()


# ПОЛУЧАТЬ Сообщения
def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']

    result = {'chat_id': chat_id, 'text': text}
    return result


# ОТПРАВЛЯТЬ Сообщения
def send_message(chat_id, text):
    import requests
    result = requests.get(URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text))
    return result
    # return "Сообщение отправленно"


flag = False
while True:
    answer = get_message()
    if not flag:
        if answer['text'] == "привет":
            send_message(chat_id=answer['chat_id'], text="И тебе привет!")
            flag = True
        if answer['text'] == "пока":
            send_message(chat_id=answer['chat_id'], text="И тебе пока!")
            flag = True
        else:
            # answer["text"] = "5+8"
            try:
                x = answer["text"].split("+")
                result = int(x[0]) + int(x[1])
                send_message(chat_id=answer['chat_id'], text=str(result))
                flag = True
            except:
                send_message(chat_id=answer['chat_id'], text="Ничего")

