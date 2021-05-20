import requests
from bs4 import BeautifulSoup
from Math_BOT.ClassBotGetUpdates import BotGetUpdates
from time import sleep
import telebot


# Возвращаем словарь с уроком из "data" с нужными данными на основе числа в "text_bot"
def get_lesson(text_bot, data):
    for k in data:
        if k['title'].split(".")[0].split(" ")[1] == text_bot:
            return k


# Проверка текста "text_bot" на наличие темы в "data"
def check_num_title(text_bot, data):
    for k in data:
        # "Тема 11. Проценты" == "11"
        if k['title'].split(".")[0].split(" ")[1] == text_bot:
            return True
    return False


# Проверяет 1- есть ли файл 2- есть ли содержимое в файле = True если ошибка равно False
def check_file():
    result = None
    with open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Math_BOT\\data.txt", "r") as file:
        result = file.read()  # Читает первые 600 символов

    if result != "":
        return True
    else:
        return False


# Парсит данные на основе списка ссылок передаваемых в url
def parse_data(url):
    temp_data = []
    for j in url:
        temp_dic = {}
        # ------- Создание BeautifulSoup -------
        _site_ = requests.get(j)
        _my_html_ = _site_.text  # Возвращает HTML ответ (всегда)
        _soup_ = BeautifulSoup(_my_html_, 'lxml')
        # ------- Парсинг -------
        try:
            title = _soup_.find_all("strong")[0].text[0:]
            url_video = _soup_.find_all("iframe")[0]["src"]
            url_forms = _soup_.find_all("iframe")[1]["src"]
            temp_dic.update({"title": title, "url_video": url_video, "url_forms": url_forms})
            temp_data.append(temp_dic)
            # print(temp_dic)
        except IndexError:
            pass
    print("Колличество удачных страниц:", len(temp_data))

    with open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Math_BOT\\data.txt", mode="w") as file:
        file.write(str(temp_data))

    return temp_data


# ------- Получаем ссылки всех тем -------

URL_SITE_5 = []
URL_SITE_6 = []

site = requests.get("https://sites.google.com/view/matema-bot/")
my_html = site.text  # Возвращает HTML ответ (всегда)
soup = BeautifulSoup(my_html, 'lxml')
lst = soup.find_all("a", "aJHbb hDrhEe HlqNPb")

for i in lst:
    if i['href'].find("5-класс") != -1:
        URL_SITE_5.append("https://sites.google.com" + i['href'])
    if i['href'].find("6-класс") != -1:
        URL_SITE_6.append("https://sites.google.com" + i['href'])

# ------- Получаем данные всех тем -------

# DATA_5 = parse_data(url=URL_SITE_5)
# print(DATA_5)

if check_file():  # Если записаные данные есть
    with open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Math_BOT\\data.txt", "r") as file:
        DATA_6 = eval(file.read())
else:  # Если записаных данных нет
    DATA_6 = parse_data(url=URL_SITE_6)
# print(DATA_6)


# ------- Работа с телеграмом -------
token = "1624243252:AAFQo5YHwdK7O2akLKZB-KyqOdTBfvBV6Zw"
requests.get(url="https://api.telegram.org/bot{}/setWebhook?url=".format(token))
bot = telebot.TeleBot(token=token)
print(bot)
bot.send_message(221824550, "Перезапуск!")


# Главный обработчик (User)
@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == "/start":
        text = "*СПИСОК ТЕМ:*\n\n"
        for i in DATA_6:
            text += "  " + i['title'] + "\n"
        text += "\n*ВЫБЕРИТЕ НОМЕР ТЕМЫ ЗАНЯТИЯ*"
        bot.send_message(chat_id=message.chat.id, text=text, parse_mode="Markdown")


bot.polling()

sleep(9999)

bot = BotGetUpdates(token="1624243252:AAFQo5YHwdK7O2akLKZB-KyqOdTBfvBV6Zw")
print("Бот запущен!")
while True:
    bot.update_json()
    bot.get_message(-1)
    print(bot.MESSAGE_INCOMING)  # Будет отображатся последнее сообщение в телеге

    if (bot.MESSAGE_INCOMING['text'] == "Привет") or (bot.MESSAGE_INCOMING['text'] == "/start") or (
            bot.MESSAGE_INCOMING['text'] == "привет"):
        chat_id = bot.MESSAGE_INCOMING["chat_id"]
        text = "*СПИСОК ТЕМ:*\n\n"

        for i in DATA_6:
            text += "  " + i['title'] + "\n"
        text += "\n*ВЫБЕРИТЕ НОМЕР ТЕМЫ ЗАНЯТИЯ*"

        bot.send_message(chat_id=chat_id, text=text, mode="Markdown")

    elif check_num_title(text_bot=bot.MESSAGE_INCOMING['text'], data=DATA_6):
        chat_id = bot.MESSAGE_INCOMING["chat_id"]
        lesson = get_lesson(text_bot=bot.MESSAGE_INCOMING['text'], data=DATA_6)

        text = "*ВЫ ВЫБРАЛИ ТЕМУ:*\n\n"
        text += lesson["title"] + "\n\n"
        text += "Просмотрите видео на эту тему: "
        text += "[{}]({})\n".format("Видео", lesson['url_video'])
        command = "/check{}".format(bot.MESSAGE_INCOMING['text'])
        text += "После проверь себя нажав: {}".format(command)
        bot.send_message(chat_id=chat_id, text=text, mode="Markdown")
    elif bot.MESSAGE_INCOMING["text"][:6] == "/check":
        chat_id = bot.MESSAGE_INCOMING["chat_id"]
        lesson = get_lesson(text_bot=bot.MESSAGE_INCOMING["text"][6:], data=DATA_6)

        text = "*ПРОВЕРЬ СЕБЯ:*\n\n"
        text += "[{}]({})".format("Форма для проверки", lesson['url_forms'])
        bot.send_message(chat_id=chat_id, text=text, mode="Markdown")

    else:
        chat_id = bot.MESSAGE_INCOMING["chat_id"]
        text = "*ТАКОЙ ТЕМЫ НЕ СУЩЕСТВУЕТ*\n\n"
        text += "Для получения списка тем, нажмите /start"
        bot.send_message(chat_id=chat_id, text=text, mode="Markdown")
