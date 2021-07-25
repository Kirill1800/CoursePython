from selenium import webdriver
from time import sleep
from InstaBot.path import path_sort, path_web_driver
from InstaBot.functions import login_inst, exception, smart_sleep, open_file_to_list, check_users
from datetime import datetime, timedelta
from InstaBot.Module2_sort import check_private


def unsubscribe(b):
    xpath1 = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button'
    smart_sleep(browser=b, xpath=xpath1)
    b.find_element_by_xpath(xpath1).click()
    xpath2 = '/html/body/div[5]/div/div/div/div[3]/button[1]'
    smart_sleep(browser=b, xpath=xpath2)
    b.find_element_by_xpath(xpath2).click()
    print("Отписались")


def module4():
    #  ----ПАРАМЕТРЫ----
    all_unsubscriptions = 720  # за сутки # 720
    unsubscriptions = 0

    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)
    sort_users = open_file_to_list(path_sort)

    # ГЛАВНЫЙ ЦИКЛ ПО ЮЗЕРАМ
    num = 0  # номер перебираемого пользователя
    start_time = datetime.now()  # время начала цикла, (тип данных это datetime)
    for person in sort_users:
        num += 1
        print()
        print("{}.".format(num), person.replace("\n", ""))  # Просто печатаем ссылку юзера
        browser.get(person)  # Заходим на ссылку юзера
        smart_sleep(browser=browser)

        res_except = exception(browser=browser)  # Проверяем рабочая ли ссылка
        res_privat = check_private(browser=browser)  # Проверяем аккаунт на приватность

        if res_except and not res_privat:  # если ссылка рабочая то:
            ch = check_users(b=browser)  # Проверяем подписаны или нет
            if ch == "Мы подписаны":
                if (datetime.now() - start_time) < timedelta(hours=1):
                    if unsubscriptions < all_unsubscriptions:
                        unsubscriptions += 1
                        unsubscribe(b=browser)  # отписываемся
                        sleep(5)
                    else:
                        print("  Предел отписок в сутки (Пауза 24 часа)")
                        sleep(87000)
                        unsubscriptions = 0
                else:
                    print("  Превышен лимит отписок в час (Пауза 2 часа)")
                    sleep(7200)
                    start_time = datetime.now()
            if ch == "Мы не подписаны":
                pass
        else:
            print("  Ошибка (Страница не найдена или приватна)")
