import json
from InstaBot.path import path_top
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_web_driver, path_top_10
from InstaBot.functions import login_inst, smart_sleep, scroll, check_users, exception
from datetime import datetime, timedelta
from InstaBot.Module2_sort import check_private
from InstaBot.Module3_like import subscribe
from termcolor import cprint
from datetime import datetime
from random import shuffle
import random


def xpath(key):
    result = {}
    # Список xpath (большой экран)
    result.update({"Строка поиска": '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]'})
    # Кнопки
    result.update({"Кнопки пользователя": '//*[@id="react-root"]/section/main/div/header/section'})
    result.update({"ПодписГ": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/button'})
    result.update({"ПодписБ": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'})
    result.update({"ОтписГ": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button'})
    result.update({"ОтписБ": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button'})
    result.update({"Подтвердить отписку": '/html/body/div[5]/div/div/div/div[3]/button[1]'})
    # Цифры
    result.update({"Подписчики": '//a[@class="-nal3 "]'})
    result.update({"Элемент скролинга": '//ul[@class="jSC57  _6xe7A"]'})
    result.update({"Подтвердить отписку3": '//button[@class="aOOlW -Cab_   "]'})
    result.update({"Подтвердить отписку4": '//button[@class="aOOlW -Cab_   "]'})
    result.update({"Подтвердить отписку5": '//button[@class="aOOlW -Cab_   "]'})
    return result[key]


def module5():
    with open(path_top, "r") as f:
        mas = json.loads(f.read())

    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(path_web_driver, options=chrome_options)

    print(0)
    login_inst(browser=browser)
    print(1)

    cprint(str(datetime.now()) + "Вход выполнен!", "green", attrs=['bold'])
    print()

    # -- 1 -- Подписатся на всех
    i = 0
    while True:
        sleep(1)

        i += 1
        shuffle(mas)  # ПЕРЕМЕШКА

        j = 0
        for user in mas:
            j += 1
            print()
            print("Человек: {}".format(user))
            browser.get(user)
            smart_sleep(browser=browser)

            res_except = exception(browser=browser)  # Проверяем рабочая ли ссылка
            res_privat = check_private(browser=browser)  # Проверяем аккаунт на приватность
            if res_except and not res_privat:  # если ссылка рабочая то:
                ch = check_users(b=browser)  # Проверяем подписаны или нет
                if ch == "Мы подписаны":
                    print("   Пропуск {} ибо подписаны!".format(user))
                if ch == "Мы не подписаны":
                    subscribe(b=browser, p=user)  # подписываемся


def module6():
    with open(path_top, "r") as f:
        mas = json.loads(f.read())

    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)

    cprint(str(datetime.now()) + "Вход выполнен!", "green", attrs=['bold'])
    print()

    # -- 2 -- Войти в свой и открыть наши подписки
    # Заходим в подписки наши
    xpath_my_sub = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
    browser.get("https://www.instagram.com/probnik6432/")
    smart_sleep(browser=browser, xpath=xpath_my_sub)
    browser.find_element_by_xpath(xpath_my_sub).click()
    # Крутим
    xpath_scroll = "/html/body/div[6]/div/div/div[3]"
    # /html/body/div[6]/div/div/div[3]
    smart_sleep(browser=browser, xpath=xpath_scroll)
    elm_scroll = browser.find_element_by_xpath(xpath=xpath_scroll)
    t = scroll(b=browser, count=100, elm_scroll=elm_scroll)  # Тут массив из пользователей (массив из элементов <li>)

    print(type(t))
    print("Число наших подписок (гортанием): {}".format(len(t)))

    while True:
        num = 0
        while num < len(t):
            num += 1
            # Нажимаем кнопку отписаться
            xpath_button_user = "/html/body/div[6]/div/div/div[3]/ul/div/li[{}]/div/div[3]/button".format(num)
            browser.find_element_by_xpath(xpath_button_user).click()
            # Подтверждаем отписку
            xpath_improve = '//button[@class="aOOlW -Cab_   "]'
            smart_sleep(browser=browser, xpath=xpath_improve)
            browser.find_element_by_xpath(xpath_improve).click()
            print("Отписались!")
            sleep(random.uniform(0.8, 1.9))
        print("---------------------")
        num = 0
        while num < len(t):
            num += 1
            # Нажимаем кнопку отписаться
            xpath_button_user = "/html/body/div[6]/div/div/div[3]/ul/div/li[{}]/div/div[3]/button".format(num)
            browser.find_element_by_xpath(xpath_button_user).click()
            print("Подписались!")
            sleep(random.uniform(0.8, 1.9))
        sleep(3)

    # -- 3 -- цикл который отписывается от всех и в тоже время опять подписывается
    # топ IDE для C++
