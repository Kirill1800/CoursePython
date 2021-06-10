from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from time import sleep
import os
from InstaBot.path import path_sort, path_subscriptions, path_webdriver
from InstaBot.functions import login_inst, exception
from datetime import datetime, timedelta


def subscribe(browser):
    sleep(2)
    browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
    print("Подписались")


#  ----ПАРАМЕТРЫ----
like_time = 10  # время между каждым лайком
all_likes = 720  # за сутки
all_subscriptions = 720  # за сутки
hour_like = 30  # число лайков за час
hour_sub = 30  # число подписок за час

#  ----В ЭТОМ ЧАСУ УЖЕ ЕСТЬ----
likes = 0
subscriptions = 0


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


browser = webdriver.Chrome(path_webdriver)
login_inst(browser=browser)

# Сформировали список из отсортированных пользователей
f = open(path_sort)
sort_users = []
for line in f:
    sort_users.append(line)
f.close()

j = 0
for person in sort_users:
    j += 1
    print(person.replace("\n", ""))

    browser.get(person)
    res_except = exception(browser=browser)

    if res_except:
        sleep(5)
        subscribe(browser=browser)
        # likes()
    else:
        print("Ошибка")

#  ----ЛИСТ С МОИМИ ПОДПИСКАМИ----
# subscriptions_list = []
# f1 = open(path_subscriptions)
# for line in f1:
#    subscriptions_list.append(line)
# f1.close()

j = 0  # номер вывода в терминале
n = 0  # пропущенное чсило совыпадений из-за совпадения в subscriptions_list
next_person = 0  # если true - следующий пользователь по циклу
start_time = datetime.now()  # время начала цикла, (тип данных это datetime)

for person in sort_users:
    # Условия паузы цикла
    if likes >= all_likes:
        print("Приделд лайков за сутки")
    else:
        pass
        likes += 1
    if subscriptions >= all_subscriptions:
        print("Придел подписок в сутки")
    else:
        pass
        subscriptions += 1
    if ((datetime.now() - start_time) >= timedelta(hours=1)) and (hour_sub <= subscriptions):
        print("Превышен лимит подписок в час")
