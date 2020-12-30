from time import sleep
from Lesson07LawrParserNBRB import LawrParserNBRB
from Lesson07LawrBotGetUpdates import LawrBotGetUpdates

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

    # Отвечаем на последние сообщение
    if (bot.MESSAGE_INCOMING['text'] == "/help") or (bot.MESSAGE_INCOMING['text'] == "/start"):
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], rates.print_help())
    if bot.MESSAGE_INCOMING['text'] == "Привет":
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], "И тебе привет!")

    sleep(2)