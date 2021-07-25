import os
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_users, path_web_driver, path_sort
from InstaBot.functions import check_good_page, login_inst, open_file_to_list


#  1) аккаунт должен быть публичным
# Проверка на приватность (True - приватный, иначе False)
def check_private(browser):
    def xpath_existence(url):
        try:
            browser.find_element_by_xpath(url)
            existence = 1
        except NoSuchElementException:
            existence = 0
        return existence

    elm = "/html/body/div[1]/section/main/div/div/article/div[1]/div/h2"
    if xpath_existence(elm) == 1:
        if browser.find_element_by_xpath(elm).text == "This Account is Private" or "Это закрытый аккаунт":
            return True
    else:
        return False


#  2) у аккаунта не может быть больше подписок, чем указано
# Проверка на колличество подписок (True - если больше count, иначе False)
def check_count_subscriptions(browser, count):
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span"  # Для открытых
        s = browser.find_element_by_xpath(elm).text
    except NoSuchElementException:
        elm = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/span/span'  # Для закрытых
        s = browser.find_element_by_xpath(elm).text

    s = s.replace(" ", "")
    s = s.replace("тыс.", "000")
    if count[0] < int(s) < count[1]:
        return True
    else:
        return False


#  3) у аккаунта не может быть больше подписчиков, чем указано
# Проверка на колличество Подпищиков (True - если больше count, иначе False)
def check_count_subscribers(browser, count):
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"  # Для открытых
        s = browser.find_element_by_xpath(elm).text
    except NoSuchElementException:
        elm = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/span/span'  # Для закрытых
        s = browser.find_element_by_xpath(elm).text

    s = s.replace(" ", "")
    s = s.replace("тыс.", "000")
    s = s.replace(",", "")
    if count[0] < int(s) < count[1]:
        return True
    else:
        return False


#  4) необходимо фото пролфиля
def chek_photo(browser):
    try:
        elm = '//*[@id="react-root"]/section/main/div/header/div/div/span/img'  # Для открытых
        s = browser.find_element_by_xpath(elm).get_attribute("src")
    except NoSuchElementException:
        elm = '//*[@id="react-root"]/section/main/div/header/div/div/div/button/img'  # Для закрытых
        s = browser.find_element_by_xpath(elm).get_attribute("src")

    if s.find("s150x150") == -1:
        if s.find("s320x320") == -1:
            return False
        else:
            return True
    else:
        return True


# Проверка на колличество ПУБЛИКАЦИЙ (True - если больше count, иначе False)
def check_count_publications(browser, count):
    elm = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
    s = browser.find_element_by_xpath(elm).text
    if int(s.replace(" ", "")) > int(count):
        return True
    else:
        return False


def module2():
    # ----- КОНСТАНТЫ -----
    acc_subscriptions = [10, 450]  # Подписки
    acc_subscribers = [10, 900]  # Подпищики
    publications = 1

    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)
    file_list = open_file_to_list(path=path_users)
    os.remove(path_sort)

    for person in file_list:
        person = person.split(". ")[1]
        print(person.replace("\n", ""))
        browser.get(person)
        sleep(1.5)

        if check_good_page(browser=browser):
            flag = False
            # Проверка
            if flag:
                print("Приватный? - ", check_private(browser=browser))
                print("Подписок больше {}? - ".format(acc_subscriptions),
                      check_count_subscriptions(browser=browser, count=acc_subscriptions))
                print("Подписчиков больше {}? - ".format(acc_subscribers),
                      check_count_subscribers(browser=browser, count=acc_subscribers))
                print("Публикаций больше {}? - ".format(publications),
                      check_count_publications(browser=browser, count=publications))
                print("Есть аватарка? - ", chek_photo(browser=browser))

            if not check_private(browser=browser):
                if check_count_subscriptions(browser=browser, count=acc_subscriptions):
                    if check_count_subscribers(browser=browser, count=acc_subscribers):
                        if check_count_publications(browser=browser, count=publications):
                            if chek_photo(browser=browser):
                                print("Человек подходит!")
                                with open(path_sort, "a") as file:
                                    file.write(person)
            print()
        else:
            print("Страница с ошибкой!")
            print()
    browser.close()


