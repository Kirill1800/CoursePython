from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from time import sleep
import os


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


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


if get_os()[1] == "Windows":
    browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\InstaBot\chrome_driver\chromedriver.exe")
else:
    browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/InstaBot/chrome_driver/chromedriver_mac64")

if get_os()[1] == "Windows":
    f = open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\InstaBot\\url_users.txt", 'r')
else:
    f = open("/Users/lawr/PycharmProjects/CoursePythonKirill/InstaBot/url_users.txt", 'r')

if get_os()[1] == "Windows":
    path_source = r"C:\Users\Admin\Documents\GitHub\CoursePython\InstaBot\"
else:
    path_source = "/Users/lawr/PycharmProjects/CoursePythonKirill/InstaBot/"

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
acc_subscriptions = [50, 450]  # Подписки
acc_subscribers = [70, 900]  # Подпищики
publications = 4


# Проверка на правильность страницы входа (открываем о тех пор пока не гуд)
while True:
    try:
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
        break
    except NoSuchElementException:
        browser.get("https://www.instagram.com/accounts/login/?source=reset_password")
        sleep(3)


t = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
t.send_keys("kirill.glushakov03@mail.ru")

sleep(3)
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input").send_keys("instapython")
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]").click()
sleep(3)

for person in file_list:
    person = person.split(". ")[1]
    j += 1
    print(person.replace("\n", ""))
    browser.get(person)
    sleep(5)

    flag = False
    # Проверка
    if flag:
        print("Приватный? - ", check_private())
        print("Подписок больше {}? - ".format(acc_subscriptions), check_count_subscriptions(count=acc_subscriptions))
        print("Подписчиков больше {}? - ".format(acc_subscribers), check_count_subscribers(count=acc_subscribers))
        print("Публикаций больше {}? - ".format(publications), check_count_publications(count=publications))
        print("Есть аватарка? - ", chek_photo())

    if not check_private():
        if check_count_subscriptions(count=acc_subscriptions):
            if check_count_subscribers(count=acc_subscribers):
                if check_count_publications(count=publications):
                    if chek_photo():

                        print(5555555555555555555555555555555555555)
                        with open(path_source + "sort_users.txt", "w") as file:
                            file.write(person)

    print()

