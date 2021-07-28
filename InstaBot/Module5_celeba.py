import json
from InstaBot.path import path_top
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_web_driver, path_top_10
from InstaBot.functions import login_inst, smart_sleep, scroll
from datetime import datetime, timedelta
from InstaBot.Module2_sort import check_private
from InstaBot.Module3_like import subscribe
from termcolor import cprint
from datetime import datetime
from random import shuffle


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
        print(type(mas), mas)

    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)

    cprint(str(datetime.now()) + "Вход выполнен!", "green", attrs=['bold'])
    print()
    i = 0

    # -- 1 -- Подписатся на всех
    # while True:
    #
    #     i += 1
    #     shuffle(mas)  # ПЕРЕМЕШКА
    #
    #     j = 0
    #     for user in mas:
    #         j += 1
    #         print()
    #         print("Человек: {}".format(user))
    #         browser.get(user)
    #         smart_sleep(browser=browser)
    #
    #         res_except = exception(browser=browser)  # Проверяем рабочая ли ссылка
    #         res_privat = check_private(browser=browser)  # Проверяем аккаунт на приватность
    #         if res_except and not res_privat:  # если ссылка рабочая то:
    #             ch = check_users(b=browser)  # Проверяем подписаны или нет
    #             if ch == "Мы подписаны":
    #                 print("   Пропуск {} ибо подписаны!".format(user))
    #             if ch == "Мы не подписаны":
    #                 print("#$^")
    #                 subscribe(b=browser, p=user)  # подписываемся

    # -- 2 -- Войти в свой и открыть наши подписки
    # Заходим в подписки наши
    xpath_my_sub = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
    browser.get("https://www.instagram.com/probnik6432/")
    smart_sleep(browser=browser, xpath=xpath_my_sub)
    browser.find_element_by_xpath(xpath_my_sub).click()
    # Крутим
    xpath_scroll = "/html/body/div[5]/div/div/div[3]"
    smart_sleep(browser=browser, xpath=xpath_scroll)
    elm_scroll = browser.find_element_by_xpath(xpath=xpath_scroll)
    t = scroll(b=browser, count=100, elm_scroll=elm_scroll)
    print(t.text)

    num = 0
    while num < len(t):
        num += 1
        # Нажимаем кнопку отписаться
        xpath_button_user = "/html/body/div[5]/div/div/div[3]/ul/div/li[{}]/div/div[2]/button".format(num)
        t.find_element_by_xpath(xpath_button_user).click()
        # Подтверждаем отписку
        xpath_improve = "/html/body/div[6]/div/div/div/div[3]/button[1]"
        smart_sleep(browser=browser, xpath=xpath_improve)
        browser.find_element_by_xpath(xpath_improve).click()

    # /html/body/div[5]/div/div/div[3]/ul/div/li[1]/div/div[2]/button
    # /html/body/div[5]/div/div/div[3]/ul/div/li[49]/div/div[2]/button
    # /html/body/div[5]/div/div/div[3]/ul/div/li[54]/div/div[2]/button

    # -- 3 -- цикл который отписывается от всех и в тоже время опять подписывается
