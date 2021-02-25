from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime

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
sleep(8)

# Запустим страницу
browser.get("https://badoo.com/encounters")
print(datetime.now(), "Ждем 20 сек")
sleep(40)

# xpath = '//use[@xlink:href="#floating-action-yes"]'  # не сработало


for i in range(10):
    try:
        xpath = '//div[@data-choice="yes"]'
        submit = browser.find_element_by_xpath(xpath=xpath)
        submit.click()
        print(datetime.now(), "Нажали на лайк")
    except ElementClickInterceptedException:
        xpath = '//div[@class="btn btn--monochrome js-chrome-pushes-deny"]'
        submit = browser.find_element_by_xpath(xpath=xpath)
        submit.click()
        print(datetime.now(), "Нажали на пропуск")
    sleep(10)


# browser.quit()
