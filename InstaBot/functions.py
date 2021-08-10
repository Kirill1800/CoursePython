from time import sleep
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import pickle


# Проверка на хорошая (true) ли страница или плохая (false)
def check_good_page(browser):
    try:
        elm = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
        smart_sleep(browser=browser, xpath=elm)
        browser.find_element_by_xpath(elm)
        return True
    except NoSuchElementException:
        return False


def login_inst(browser, username="kirill.glushakov03@mail.ru", password="instapython"):

    # ВХОД НА СТРАНИЦУ ВХОДА В ИНСТАГРАМ
    def open_inst():
        while True:  # Проверка на правильность страницы входа (открываем о тех пор пока не гуд)
            try:
                browser.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
                break
            except NoSuchElementException:
                browser.get("https://www.instagram.com/accounts/edit/")
                sleep(1)

    open_inst()
    xpath_try_login = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div'
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))  # Открытие cookies
        for cookie in cookies:
            browser.add_cookie(cookie)
        # Открытие стандартной страницы
        browser.get("https://www.instagram.com/slutskgorod/")
        smart_sleep(browser=browser, xpath=xpath_try_login)
    except FileNotFoundError:
        # ВХОД В АККАУНТ
        xpath_user_name = "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input"
        xpath_password = "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input"
        xpath_button = "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]"
        # ЛОГИН
        browser.find_element_by_xpath(xpath_user_name).send_keys(username)
        # ПАРОЛЬ
        browser.find_element_by_xpath(xpath_password).send_keys(password)
        browser.find_element_by_xpath(xpath_button).click()
        smart_sleep(browser=browser, xpath=xpath_try_login)
        # Открытие стандартной страницы
        browser.get("https://www.instagram.com/slutskgorod/")
        smart_sleep(browser=browser, xpath=xpath_try_login)
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))


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
        while (datetime.now() - start_time) < timedelta(seconds=8):
            try:
                browser.find_element_by_xpath(xpath=capture_inst_xpath)
                if xpath is not None:
                    browser.find_element_by_xpath(xpath=xpath)
                print("  smart_sleep {}".format(datetime.now() - start_time))
                return True
            except NoSuchElementException:
                sleep(0.0001)
        return False


# Открытие файла и добавление всех строчек файла в LIST и вернуть LIST
def open_file_to_list(path):
    f = open(path, 'r')
    file_list = []
    for line in f:
        file_list.append(line)
    f.close()
    return file_list


def text_to_list(lst, count):
    txt = ""
    count = 0
    for line in lst:
        if count < 10:
            txt += line
        count += 1
    return txt


#  проверка подписаны мы на человека или нет
def check_users(b):
    xpath = '//button[@class="sqdOP  L3NKy   y3zKF     "]'  # синяя кнопка подписатся
    try:
        result = "Мы не подписаны"
        smart_sleep(browser=b, xpath=xpath)
        b.find_element_by_xpath(xpath)
        return result
    except NoSuchElementException:
        result = "Мы подписаны"
        return result


# Поиск элемента по "xpath" или "name" (в случае ошибки напечатает "text" если он указан)
def find_element(b, text=None, xpath=None, name=None, delay=True):
    def recursion():
        sleep(0.1)
        try:
            if datetime.now() - time > timedelta(seconds=4):
                return None
            else:
                if name is not None:
                    answer = b.find_element_by_name(name)
                    return answer
                if xpath is not None:
                    answer = b.find_element_by_xpath(xpath)
                    return answer
        except NoSuchElementException:
            return recursion()

    # Искать с задержкой (Много раз)
    if delay:
        time = datetime.now()
        result = recursion()
        if result is None:
            if text is not None:
                print("ERROR", "NoSuchElement", "({}) | Delay = {}".format(text, 4))
            return result
        else:
            return result
    # Искать сразу (один раз)
    else:
        if name is not None:
            try:
                return b.find_element_by_name(name)
            except NoSuchElementException:
                return None
        if xpath is not None:
            try:
                return b.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None


# Прокрутка до того момента пока не наберется число "count" пользователей | прокручиваемый элемент "elm_scroll"
def scroll(b, count, elm_scroll):

    xpath_count_my_sub = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span'
    xpath_count_parse_users_li = '/html/body/div[6]/div/div/div[3]/ul/div/li'
    count_my_sub = b.find_element_by_xpath(xpath_count_my_sub).text
    count_my_sub = count_my_sub.replace(" ", "")
    count_my_sub = count_my_sub.replace("тыс.", "000")
    count_my_sub = int(count_my_sub)
    print("Число наших подписок (из цифры):", count_my_sub)

    # Ограничение на парсинг пользователей при прокрутке
    if count > count_my_sub:
        temp_count = count_my_sub
    else:
        temp_count = count

    while True:
        sleep(0.5)
        b.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight; """, elm_scroll)
        elms_users = b.find_elements_by_xpath(xpath_count_parse_users_li)

        if len(elms_users) >= temp_count:
            return elms_users
