from time import sleep
from Lesson07LawrParserNBRB import ParserNBRB
from Lesson07LawrBotGetUpdates import BotGetUpdates
import random

sleep(5)  # Заснет на 5 секунд

# Создание Объектов (бот и парсер)
bot = BotGetUpdates("1420906671:AAFYtk31Zd2Ftyqc58S4hJVJFzL0FO3TVUs")  # создание бота
rates = ParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")  # создание парсера

number_random = None
number_input = None
flag_game = False

# Запускаем бесконечный цикл
while True:
    sleep(2)

    # Обновление Данных (первоначально данные все в JSON)
    rates.update_json()
    bot.update_json()

    # Получаем последнее сообщение -> Формируем "self.MESSAGE_INCOMING"
    bot.get_message(-1)
    # print(bot.MESSAGE_INCOMING)

    #  Отвечаем на последние сообщение

    if flag_game:

        try:
            number_input = int(bot.MESSAGE_INCOMING['text'])

            if number_random == number_input:
                bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Игра остановлена. Вы угадали число.')
            elif number_random > number_input:
                bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Игра остановлена. Число слишком маленькое. {}'.format(str(number_random)))
            elif number_random < number_input:
                bot.send_message(bot.MESSAGE_INCOMING['chat_id'], 'Игра остановлена. Число слишком большое. {}'.format(str(number_random)))
            flag_game = False

        except ValueError:
            pass

    else:

        # Чтобы не писать много "if" генерируем основании списка полученного из rates.list_cur_abbreviation()
        for cur_abb in rates.list_cur_abbreviation():
            if bot.MESSAGE_INCOMING['text'] == "/" + cur_abb.swapcase():
                bot.send_message(bot.MESSAGE_INCOMING['chat_id'], rates.print_money(rates.get_money(cur_abb)))

        if (bot.MESSAGE_INCOMING['text'] == "/help") or (bot.MESSAGE_INCOMING['text'] == "/start"):
            bot.send_message(bot.MESSAGE_INCOMING['chat_id'], rates.print_help())
        elif bot.MESSAGE_INCOMING['text'] == "Привет":
            bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "И тебе привет!")
        elif bot.MESSAGE_INCOMING['text'] == "Пока":
            bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "Удачи, пока!")
        elif bot.MESSAGE_INCOMING['text'] == "/play":
            flag_game = True
            number_random = random.randint(1, 20)
            bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "Игра запущена. Введите число от 1 до 20")