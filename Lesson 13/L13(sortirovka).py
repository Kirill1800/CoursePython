from selenium import webdriver
from time import sleep

days = 20
acc_subsckriptions = 200
publications = 10
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\Lesson 13\chrome_driver\chromedriver.exe")

f = open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Lesson 13\\temp.txt", 'r')
file_list = []
for line in f:
    file_list.append(line)
f.close()

#  ОБРАБОТКА ССЫЛОК

#  1) аккаунт должен быть публичным
#  2) у аккаунта не может быть больше подписчиков, чем указано
#  3) не должно быть ссылки на сайт
#  4) необходимо фото пролфиля
#  5) не менее 5 публикаций
#  6) посленяя публикация не менее days дней назад

filter_list = []
i = 0  # подходят
j = 0  # на выходе

for person in file_list:
    j += 1
    browser.get(person)
    sleep(0.5)

element = "/html/body/div[1]/section/main/div/div/article/div[1]/div/h2"
if xpath_existence(element) == 1:
    try:
        if browser.find_element_by_xpath(element).text == "This Account is Private" or "Это закрытый аккаунт":
            print(j, "Приватный аккаунт")
            continue
    except StaleElementReferenceException:
        print("Ошибка")

element = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/span/span"
if xpath_existence(element) == 0:
    print("Ошибка 2")
    continue
status = browser.find_element_by_xpath(element).text
if int(status) > acc_subsckriptions:
    print(j, "У аккаунта слишком много подписчиков")
    continue

element = "/html/body/div[1]/section/main/div/header/section/div[2]"
if xpath_existence(element) == 1:
    print(j, "Есть ссылка на сайт")
    continue

element = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
if xpath_existence(element) == 0:
    print(j, "Ошибка 3")
    continue
status = browser.find_element_by_xpath(element).text
if int(status) < publications:
    print(j, "Мало публикаций")
    continue
