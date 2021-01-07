from time import sleep
from Lesson07LawrParserNBRB import LawrParserNBRB
from Lesson07LawrBotGetUpdates import LawrBotGetUpdates
import random

sleep(5)  # Заснет на 5 секунд

# Создание Объектов (бот и парсер)
bot = LawrBotGetUpdates("1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs")  # создание бота
rates = LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")  # создание парсера

# Запускаем бесконечный цикл
while True:

    # Обновление Данных (первоначально данные все в JSON)
    rates.update_json()
    bot.update_json()

    # Получаем последнее сообщение -> Формируем "self.MESSAGE_INCOMING"
    bot.get_message(-1)
    print(bot.MESSAGE_INCOMING)
    #  Отвечаем на последние сообщение
    if (bot.MESSAGE_INCOMING['text'] == "/help") or (bot.MESSAGE_INCOMING['text'] == "/start"):
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], rates.print_help())
    if bot.MESSAGE_INCOMING['text'] == "Привет":
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "И тебе привет!")
    if bot.MESSAGE_INCOMING['text'] == "Пока":
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "Удачи, пока!")
    if bot.MESSAGE_INCOMING['text'] == "/play":
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "Введите число от 1 до 20")
number = random.randint(1, 20)
guesses = 0
while guesses < 3:
    bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "Введите число от 1 до 20")
    guess = int(input())  # вводим число
    guesses += 1  # увеличиваем попытку
    if bot.MESSAGE_INCOMING[int('text')] == number:
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Успех!')
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Вы угадали число. ' + str(guesses))
        break
    elif bot.MESSAGE_INCOMING[int('text')] < number:
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Число слишком маленькое. Попробуй еще.')
    elif bot.MESSAGE_INCOMING[int('text')] > number:
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Число слишком большое. Попробуй еще.')
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Ты не угадал число. Исходное число: ' + str(number))

    sleep(2)
