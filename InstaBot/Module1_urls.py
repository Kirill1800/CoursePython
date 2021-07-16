from selenium import webdriver
from time import sleep
from InstaBot.path import path_users, path_web_driver
from InstaBot.functions import login_inst, smart_sleep


# открытие подпищиков
def open_subscribers(b):
    xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
    smart_sleep(browser=b, xpath=xpath)
    b.find_element_by_xpath(xpath).click()  # открытие подписчиков
    print("Открыли подпищиков")


# получение подпищиков (вместе с прокруткой)
def get_subscribes(b, count):
    result = []

    elm = b.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    sleep(3)

    while True:
        sleep(0.5)
        b.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight; """, elm)
        elms_users = b.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
        if len(elms_users) >= count:
            break

    n = 0
    for user in elms_users:
        n += 1
        if n <= count:
            result.append(user.get_attribute("href"))

    return result


# ГЛАВНЫЙ ЗАПУСК МОДУЛЯ 1
def main():
    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)
    open_subscribers(b=browser)
    url_subscribes = get_subscribes(b=browser, count=200)  # Получение и Прокрутка подпишиков
    # создание файла со списком пользователей
    with open(path_users, "w") as file:
        n = 1
        for i in url_subscribes:
            file.write(str(n) + ". " + str(i) + "\n")
            n += 1
    print("Записаны пользователи")
    browser.close()
