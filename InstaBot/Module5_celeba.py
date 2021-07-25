import json
from InstaBot.path import path_top
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_sort, path_subscriptions, path_web_driver
from InstaBot.functions import login_inst, find_element, exception, smart_sleep, open_file_to_list, check_users
from datetime import datetime, timedelta
from InstaBot.Module2_sort import check_private
from termcolor import cprint
from datetime import datetime
from random import shuffle


def xpath(key):
    result = {}
    # Список xpath (большой экран)
    result.update({"Строка поиска": '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]'})
    # Кнопки
    result.update({"Кнопки пользователя": '//*[@id="react-root"]/section/main/div/header/section'})
    result.update({"Подписаться": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/button'})
    # без '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'
    # галка //*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/button
    result.update(
        {"Отписатся": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button'})
    # //*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button
    result.update({"Подтвердить отписку": '/html/body/div[5]/div/div/div/div[3]/button[1]'})
    # /html/body/div[5]/div/div/div/div[3]/button[1]
    # Цифры
    result.update({"Подписчики": '//a[@class="-nal3 "]'})
    result.update({"Элемент скролинга": '//ul[@class="jSC57  _6xe7A"]'})
    result.update({"Подтвердить отписку3": '//button[@class="aOOlW -Cab_   "]'})
    result.update({"Подтвердить отписку4": '//button[@class="aOOlW -Cab_   "]'})
    result.update({"Подтвердить отписку5": '//button[@class="aOOlW -Cab_   "]'})
    return result[key]


# ПОДПИСАТЬСЯ (True - подписался, False - не получилось)
def subscribe(browser):
    find_element(b=browser, xpath=xpath("Строка поиска"), text="Строка поиска")
    try:
        # sleep(9999)
        find_element(b=browser, xpath=xpath("Подписаться"), text="Кнопка Подписаться").click()
        # Проверка
        if find_element(b=browser, xpath=xpath("Отписатся"), text="Кнопка Отписаться") is not None:
            return True
        else:
            return False
    except AttributeError:
        return False


# ОТПИСАТЬСЯ (True - отписался, False - не получилось)
def unsubscribe(browser):
    find_element(b=browser, xpath=xpath("Строка поиска"), text="Строка поиска")
    try:
        find_element(b=browser, xpath=xpath("Отписатся"), text="Кнопка Отписаться").click()
        find_element(b=browser, xpath=xpath("Подтвердить отписку"), text="Кнопка подтвердить отписку").click()
        # Проверка
        if find_element(b=browser, xpath=xpath("Подписаться"), text="Кнопка Подписаться") is not None:
            return True
        else:
            return False
    except AttributeError:
        return False


def module5():
    with open(path_top, "r") as f:
        mas = json.loads(f.read())
        print(type(mas), mas)

    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)

    cprint(str(datetime.now()) + "Вход выполнен!", "green", attrs=['bold'])
    print()
    i = 0
    count_subscribe = 0
    count_unsubscribe = 0
    while True:
        i += 1
        shuffle(mas)  # ПЕРЕМЕШКА
        # mas = ["https://www.instagram.com/zendaya/"]
        j = 0
        for user in mas:
            j += 1
            browser.get(user)
            find_element(b=browser, xpath=xpath("Кнопки пользователя"), text="Кнопки пользователя")
            # sleep(9999)

            # if find_element(b=browser, xpath='//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[2]/div/span/span[1]/button/div/span', text="Кнопка отписаться", not_delay=True) is not None:
            #     print("Мы НЕ подписаны на этого человека")
            #     # self.subscribe()
            # else:
            #     print("Мы подписаны на этого человека")
            #     # self.unsubscribe()
            # sleep(10000000)

            print()
            # Если подписаны
            if find_element(b=browser, xpath=xpath("Подписаться")):
                cprint("[ИНФО] Мы подписаны на этого человека", "red")
                if subscribe(browser):
                    cprint("[ДЕЙСТВИЕ] Подписались", "red")
                    cprint("[ИНФО] Подписались {} из {}".format(j, len(mas)), "red")
            else:
                cprint("[ИНФО] Мы НЕ подписаны на этого человека", "red")
                if unsubscribe(browser):
                    text = "[ДЕЙСТВИЕ] Отписался от {}".format(user.rsplit('/')[3])
                    count = "{0:0>2}".format(i) + "." + "{0:0>3}".format(j)
                    cprint(str(datetime.now()) + count + " " + text, "green", attrs=['bold'])
                    count_unsubscribe += 1
                sleep(1.5)
                if subscribe(browser):
                    # num = self.top_users(user, 500, flag="MY_NUM", my_name=account)
                    num = 0
                    text = "[ДЕЙСТВИЕ] Подписался на {} (Теперь я №{} сверху)".format(user.rsplit('/')[3], num)
                    count = "{0:0>2}".format(i) + "." + "{0:0>3}".format(j)
                    cprint(str(datetime.now()) + count + " " + text, "green", attrs=['bold'])
                    count_subscribe += 1


module5()
