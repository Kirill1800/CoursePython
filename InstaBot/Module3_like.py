from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_sort, path_subscriptions, path_web_driver
from InstaBot.functions import login_inst, exception, smart_sleep
from datetime import datetime, timedelta


# Проверка на приватность (True - приватный, иначе False)
def check_private(b):
    elm = "/html/body/div[1]/section/main/div/div/article/div[1]/div/h2"
    if xpath_existence(elm) == 1:
        if b.find_element_by_xpath(elm).text == "This Account is Private" or "Это закрытый аккаунт":
            return True
    else:
        return False


# Подписались на человека
def subscribe(b, p):
    xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'
    smart_sleep(browser=b, xpath=xpath)
    b.find_element_by_xpath(xpath).click()
    print("  Подписались")
    with open(path_subscriptions, mode="a") as file:
        file.write(str(p))


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


#  проверка подписаны мы на человека или нет
def check_users(b):
    xpath_yes_subscribe = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div/span'
    try:
        result = "Мы подписаны"
        b.find_element_by_xpath(xpath_yes_subscribe)
        print("  " + result)
        return result
    except NoSuchElementException:
        result = "Мы не подписаны"
        print("  " + result)
        return result


# Поставить лайк первой публикации
def like(b):
    sleep(3)
    xpath = '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a'
    try:
        url = b.find_element_by_xpath(xpath).get_attribute('href')
        print("  Поставили лайк публикации {}".format(url))
        browser.get(url=url)
        xpath1 = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button'
        smart_sleep(browser=b, xpath=xpath1)
        b.find_element_by_xpath(xpath1).click()
        sleep(5)
    except NoSuchElementException:
        print("  НЕ Поставили лайк (не нашли публикацию)")


#  ----ПАРАМЕТРЫ----
like_time = 10  # время между каждым лайком
all_likes = 720  # за сутки
all_subscriptions = 5  # за сутки # 720
hour_like = 30  # число лайков за час
hour_sub = 30  # число подписок за час

browser = webdriver.Chrome(path_web_driver)
login_inst(browser=browser)

# Сформировали список из отсортированных пользователей
f = open(path_sort)
sort_users = []
for line in f:
    sort_users.append(line)
f.close()

#  ----В ЭТОМ ЧАСУ УЖЕ ЕСТЬ----
likes = 0
subscriptions = 0

num = 0  # номер перебираемого пользователя
start_time = datetime.now()  # время начала цикла, (тип данных это datetime)

# ГЛАВНЫЙ ЦИКЛ ПО ЮЗЕРАМ
for person in sort_users:
    num += 1
    print()
    print("{}.".format(num), person.replace("\n", ""))  # Просто печатаем ссылку юзера
    browser.get(person)  # Заходим на ссылку юзера
    smart_sleep(browser=browser)

    res_except = exception(browser=browser)  # Проверяем рабочая ли ссылка
    res_privat = check_private(b=browser)  # Проверяем аккаунт на приватность

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
# КОНЕЦ НАШЕГО ГЛАВНОГО ЦИКЛА
