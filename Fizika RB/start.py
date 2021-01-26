from time import sleep
from ClassBotGetUpdates import BotGetUpdates
from ClassParser import titles, values
import random

# Создание Объектов (бот и парсер)
bot = BotGetUpdates("1590868365:AAGNiNHekNVgKxIt1SVgTm3RuQFMmynidPA")  # создание бота

lst_commands = []
for i in values:
    try:
        lst_commands.append("/" + i[0].split("(")[1].replace(")", ""))
    except IndexError:
        pass

print(lst_commands)

# Запускаем бесконечный цикл
while True:
    bot.update_json()
    bot.get_message(-1)
    # print(bot.MESSAGE_INCOMING['text'])

    #  Отвечаем на последние сообщение
    if (bot.MESSAGE_INCOMING['text'] == "/help") or (bot.MESSAGE_INCOMING['text'] == "/start"):
        text = "СПИСОК АСТЕРОИДОВ:\n"
        for i in values:
            try:
                text += "/" + i[0].split("(")[1].replace(")", "") + "  "
            except IndexError:
                pass
        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], text)
    for cmd in lst_commands:
        text = ""
        if bot.MESSAGE_INCOMING['text'] == cmd:
            j = 0
            for i in values:
                try:
                    if "/" + i[0].split("(")[1].replace(")", "") == cmd:
                        # ##########
                        text = ""
                        count = 0
                        for i in titles:
                            if count <= 1:
                                text += titles[count] + " : " + values[j][count] + "\n"
                            elif count == 2:
                                text += titles[count] + " : " + values[j][count] + "-" + values[0][count + 1] + "\n"
                            else:
                                text += titles[count] + " : " + values[j][count + 1] + "\n"
                            count += 1
                        bot.send_message(bot.MESSAGE_INCOMING['chat_id'], text)
                        # ##########
                    j += 1
                except IndexError:
                    pass

