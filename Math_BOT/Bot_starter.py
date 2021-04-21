import random
import os
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup

# # ------- Создание Chrome -------
# if get_os()[1] == "Windows":
#     browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\Math_BOT\chrome_driver\chromedriver.exe")
# else:
#     browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/Math_BOT/chrome_driver/chromedriver_mac64")


# Возвращает "Unix" или "Windows" и Разделитель(separator)
def get_os():
    # Примеры разных путей: 'C:\\Users\\Administrator\\__file__' or '/Users/lawr/PycharmProjects/FrxBot/__file__'
    path = os.path.realpath('__file__')
    # Linux / MacOS
    if path[0] == "/":
        if path[2] != "\\":
            return "/", "Unix"
    # Windows
    if path[0] != "/":
        if path[2] == "\\":
            return "\\", "Windows"

# ------- Получаем ссылки всех тем -------

URL_SITE_5 = []
URL_SITE_6 = []

site = requests.get("https://sites.google.com/view/matema-bot/")
my_html = site.text  # Возвращает HTML ответ (всегда)
soup = BeautifulSoup(my_html, 'lxml')
lst = soup.find_all("a", "aJHbb hDrhEe HlqNPb")

for i in lst:
    if i['href'].find("5-класс") != -1:
        URL_SITE_5.append("https://sites.google.com" + i['href'])
    if i['href'].find("6-класс") != -1:
        URL_SITE_6.append("https://sites.google.com" + i['href'])

# print(URL_SITE_5)
# print()
# print(URL_SITE_6)

for i in URL_SITE_6:
    # ------- Создание BeautifulSoup -------
    site = requests.get(i)
    my_html = site.text  # Возвращает HTML ответ (всегда)
    soup = BeautifulSoup(my_html, 'lxml')

    # ------- Парсинг -------
    title = None
    url_video = soup.find_all("iframe")[0]["src"]
    url_forms = soup.find_all("iframe")[1]["src"]

    print(title, url_video, url_forms)


# # Запустим страницу
# browser.get(URL_SITE)
# sleep(3)
#
# print(browser.find_element_by_xpath('a').text)

# elm_video = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/a')
# elm_video = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/a')


# print(elm_video['href'])


# t.send_keys("kirill.glushakov03@mail.ru")
#
# sleep(3)
# browser.find_element_by_xpath(
#     "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input").send_keys("instapython")
# browser.find_element_by_xpath(
#     "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]").click()
# sleep(3)
#
# browser.get("https://www.instagram.com/natgeo/")
# sleep(3)