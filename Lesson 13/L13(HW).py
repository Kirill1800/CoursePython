from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

#  def check_full_page(_xpath):
#  time = 0
#  while time <= 60:
#  try:
#  browser.find_element_by_xpath(xpath=_xpath)
#  return True
#  except ElementClickInterceptedException:
#  sleep(0.5)
#  except NoSuchElementException:
#  sleep(0.5)
#  time += 0.5
#  return False


browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/Lesson 13/chrome_driver/chromedriver_mac64")
# browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\Lesson 13\chrome_driver\chromedriver.exe")

print(browser)

# Запустим страницу
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

browser.get("https://www.instagram.com/natgeo/")
sleep(3)

browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()  # открытие подписчиков

sleep(3)


def new_scroll_element(e):
    const = 30000
    ht = 0
    i = 0
    while const >= ht:
        sleep(0.5)
        ht = browser.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight;
                        """, e)
        print(ht)
        print(browser.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')[i].get_attribute("href"))
        sleep(0.5)
        i += 1


def get_subscribes(elm, count):
    result = []

    while True:
        sleep(0.5)
        browser.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight; """, elm)
        elms_users = browser.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
        if len(elms_users) >= count:
            break

    n = 0
    for user in elms_users:
        n += 1
        if n <= count:
            result.append(user.get_attribute("href"))

    return result


# Прокрутка подпишиков
elm_subscribes = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
# new_scroll_element(elm_subscribes)
sleep(3)
url_subscribes = get_subscribes(elm=elm_subscribes, count=200)

# создание файла со списком пользователей
with open("temp.txt", "w") as file:
    n = 1
    for i in url_subscribes:
        file.write(str(n) + ". " + str(i) + "\n")
        n += 1
