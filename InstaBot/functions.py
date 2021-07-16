from time import sleep
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta


# Проверка на хорошая (true) ли страница или плохая (false)
def check_good_page(browser):
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
        browser.find_element_by_xpath(elm)
        return True
    except NoSuchElementException:
        return False


def login_inst(browser, username="kirill.glushakov03@mail.ru", password="instapython"):
    # Запустим страницу

    # Проверка на правильность страницы входа (открываем о тех пор пока не гуд)
    while True:
        try:
            browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
            break
        except NoSuchElementException:
            browser.get("https://www.instagram.com/accounts/login/?source=reset_password")
            sleep(3)

    # ЛОГИН
    t = browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
    t.send_keys(username)
    sleep(3)
    # ПАРОЛЬ
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input").send_keys(password)
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]").click()
    sleep(3)
    # Открытие стандартной страницы
    browser.get("https://www.instagram.com/slutskgorod/")
    sleep(3)


# Обработка ошибок запроса к сайту, если ошибок нет - True иначе - False
def exception(browser):
    # Ошибка 560
    # try:
    #    elm = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[2]"  # Ошибка 560
    #    s = browser.find_element_by_xpath(elm).text
    #    print(s)
    #    return False
    # except:
    #    pass

    # К сожалению, эта страница недоступна.
    # try:
    #    elm = '//*[@id="react-root"]/section/main/div/h2'
    #    s = browser.find_element_by_xpath(elm).text
    #    print(s)
    #    return False
    # except:
    #    pass

    # Универсально (Поиск надписи подпищиков)
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
        browser.find_element_by_xpath(elm)
        return True
    except NoSuchElementException:
        return False


# Функция которая ищет 60 секунд элемент и если не находит False, если находит True
def smart_sleep(browser, xpath=None, strict_pause=None):
    if strict_pause is not None:
        sleep(strict_pause)
        return True
    else:
        capture_inst_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img'
        start_time = datetime.now()
        while (datetime.now() - start_time) < timedelta(minutes=1):
            try:
                browser.find_element_by_xpath(xpath=capture_inst_xpath)
                if xpath is not None:
                    browser.find_element_by_xpath(xpath=xpath)
                print("  smart_sleep {}".format(datetime.now() - start_time))
                return True
            except NoSuchElementException:
                sleep(0.0001)
        return False
