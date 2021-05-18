from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from time import sleep
import os

#  ----ПАРАМЕТРЫ----
like_time = 10  # время между каждыфм лайком
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


#  browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/InstaBot/chrome_driver/chromedriver_mac64")
browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\InstaBot\chrome_driver\chromedriver.exe")

print(browser)

# Запустим страницу
browser.get("https://www.instagram.com/accounts/login/?source=reset_password")
sleep(3)

t = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
t.send_keys("kirill.glushakov03@mail.ru")

sleep(3)
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input").send_keys("instapython")
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]").click()
sleep(3)

f = open(r"C:\Users\Admin\Documents\GitHub\CoursePython\InstaBot\sort_users.txt")

file_list = []
for line in f:
    file_list.append(line)
f.close()

#  ----ЛИСТ С МОИММИ ПОДПИСКАМИ----
subscriptions_list = []
f1 = open(r"C:\Users\Admin\Documents\GitHub\CoursePython\InstaBot\subscriptions.txt")
for line in f1:
    subscriptions_list.append(line)
f1.close()

j = 0  # номер вывода в терминале
n = 0  # пропущенное чсило совыпадений из-за совпадения в subscriptions_list

