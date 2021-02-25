from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


# Функция которая ищет 60 секунд элемент и если не находит False, если находит True
def check_full_page(_xpath):
    time = 0
    while time <= 60:
        try:
            browser.find_element_by_xpath(xpath=_xpath)
            return True
        except ElementClickInterceptedException:
            sleep(0.5)
        except NoSuchElementException:
            sleep(0.5)
        time += 0.5
    return False


# Данные для входа
# kirill.glushakov03@mail.ru : badoopython03


# Создали браузер
browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/Lesson 13/chrome_driver/chromedriver_mac64")

print(browser)

# Запустим страницу
browser.get("https://badoo.com/ru/signin/")
sleep(1)

# Ввод емейл
input_email = browser.find_element_by_name('email')
sleep(1)
input_email.send_keys('kirill.glushakov03@mail.ru')
sleep(1)

# Ввод пароля
input_email = browser.find_element_by_name('password')
sleep(1)
input_email.send_keys('badoopython03')
sleep(1)

# Нажатие кнопки входа
submit = browser.find_element_by_name('post')
submit.click()
sleep(15)

# Запустим страницу
browser.get("https://badoo.com/encounters")

if check_full_page('//div[@data-choice="yes"]'):
    for i in range(30):
        sleep(1)
        try:
            if check_full_page('//div[@data-choice="yes"]'):
                xpath = '//div[@data-choice="yes"]'
                submit = browser.find_element_by_xpath(xpath=xpath)
                submit.click()
                print(datetime.now(), "Нажали на лайк")
        except ElementClickInterceptedException:
            if check_full_page('//div[@class="btn btn--monochrome js-chrome-pushes-deny"]'):
                xpath = '//div[@class="btn btn--monochrome js-chrome-pushes-deny"]'
                submit = browser.find_element_by_xpath(xpath=xpath)
                submit.click()
                print(datetime.now(), "Нажали на пропуск")

# browser.quit()


