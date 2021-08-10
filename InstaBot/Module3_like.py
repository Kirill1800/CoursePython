from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_sort, path_subscriptions, path_web_driver
from InstaBot.functions import login_inst, exception, smart_sleep, open_file_to_list, check_users
from datetime import datetime, timedelta
from InstaBot.Module2_sort import check_private


# Подписались на человека
def subscribe(b, p):
    xpath = '//button[@class="sqdOP  L3NKy   y3zKF     "]'
    smart_sleep(browser=b, xpath=xpath)
    b.find_element_by_xpath(xpath).click()
    print("  Подписались")
    # w - перезаписат | a - добавить | r - прочитать
    with open(path_subscriptions, mode="w") as file:
        file.write(str(p))


# Поставить лайк первой публикации
def like(b):
    sleep(3)
    xpath = '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a'
    try:
        url = b.find_element_by_xpath(xpath).get_attribute('href')
        print("  Поставили лайк публикации {}".format(url))
        b.get(url=url)
        xpath1 = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button'
        smart_sleep(browser=b, xpath=xpath1)
        b.find_element_by_xpath(xpath1).click()
    except NoSuchElementException:
        print("  НЕ Поставили лайк (не нашли публикацию)")


def module3():
    #  ----ПАРАМЕТРЫ----
    all_likes = 720  # за сутки
    all_subscriptions = 5  # за сутки # 720
    #  ----В ЭТОМ ЧАСУ УЖЕ ЕСТЬ----
    likes = 0
    subscriptions = 0

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
                pass
            if ch == "Мы не подписаны":
                if (datetime.now() - start_time) < timedelta(hours=1):
                    if subscriptions < all_subscriptions:
                        subscriptions += 1
                        subscribe(b=browser, p=person)  # подписываемся
                        sleep(5)
                        if likes < all_likes:
                            likes += 1
                            like(b=browser)  # ставим лайк
                            sleep(5)
                        else:
                            print("Пределд лайков за сутки (Пауза 24 часа)")
                            sleep(87000)
                            likes = 0
                    else:
                        print("  Предел подписок в сутки (Пауза 24 часа)")
                        sleep(87000)
                        subscriptions = 0
                else:
                    print("  Превышен лимит подписок в час (Пауза 2 часа)")
                    sleep(7200)
                    start_time = datetime.now()
        else:
            print("  Ошибка (Страница не найдена или приватна)")
