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


while True:
    print(get_message())
    sleep(2)
