from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from time import sleep
import os
from InstaBot.path import path_users, path_webdriver, path_sort
from InstaBot.functions import login_inst, exception


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


browser = webdriver.Chrome(path_webdriver)
f = open(path_users, 'r')

file_list = []
for line in f:
    file_list.append(line)
f.close()


# file_list = ["1. https://www.instagram.com/fiydarigno/", "3. https://www.instagram.com/rosa_chot1/"]


#  ------------------- ОБРАБОТКА ССЫЛОК -------------------


#  1) аккаунт должен быть публичным
# Проверка на приватность (True - приватный, иначе False)
def check_private():
    elm = "/html/body/div[1]/section/main/div/div/article/div[1]/div/h2"
    if xpath_existence(elm) == 1:
        if browser.find_element_by_xpath(elm).text == "This Account is Private" or "Это закрытый аккаунт":
            return True
    else:
        return False


#  2) у аккаунта не может быть больше подписчиков, чем указано
# Проверка на колличество подписок (True - если больше count, иначе False)
def check_count_subscriptions(count):
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
def check_count_subscribers(count):
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"  # Для открытых
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


#  3) не должно быть ссылки на сайт
#  4) необходимо фото пролфиля
def chek_photo():
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


#  5) не менее 5 публикаций

# Проверка на колличество подписок (True - если больше count, иначе False)
def check_count_publications(count):
    elm = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
    s = browser.find_element_by_xpath(elm).text
    if int(s.replace(" ", "")) > int(count):
        return True
    else:
        return False


filter_list = []
i = 0  # подходят
j = 0  # на выходе

# ----- КОНСТАНТЫ -----
acc_subscriptions = [10, 450]  # Подписки
acc_subscribers = [10, 900]  # Подпищики
publications = 1

login_inst(browser=browser)

os.remove(path_sort)

for person in file_list:
    person = person.split(". ")[1]
    j += 1
    print(person.replace("\n", ""))

    browser.get(person)
    res_except = exception(browser=browser)

    if res_except:
        sleep(5)
        flag = False
        # Проверка
        if flag:
            print("Приватный? - ", check_private())
            print("Подписок больше {}? - ".format(acc_subscriptions),
                  check_count_subscriptions(count=acc_subscriptions))
            print("Подписчиков больше {}? - ".format(acc_subscribers), check_count_subscribers(count=acc_subscribers))
            print("Публикаций больше {}? - ".format(publications), check_count_publications(count=publications))
            print("Есть аватарка? - ", chek_photo())

        if not check_private():
            if check_count_subscriptions(count=acc_subscriptions):
                if check_count_subscribers(count=acc_subscribers):
                    if check_count_publications(count=publications):
                        if chek_photo():
                            print("Аккаунт подходит!")
                            with open(path_sort, "a") as file:
                                file.write(person)

        print()
    else:
        print("Ошибка. Пропуск человека!")
        print()
