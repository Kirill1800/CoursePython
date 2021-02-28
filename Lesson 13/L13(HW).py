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

full = 100

browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\Lesson 13\chrome_driver\chromedriver.exe")

print(browser)

# Запустим страницу
browser.get("https://www.instagram.com/accounts/login/?source=reset_password")
sleep(3)

browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input").send_keys(
    "name")
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[2]/div/label/input").send_keys("password")
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]").click()
sleep(3)

browser.get("https://www.instagram.com/natgeo/")
sleep(3)

browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()  # открытие подписчиков

element = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")  # прокручиваемый элемент
# начальная прокрутка, плавная прокрутка
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" % 6, element)
sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" % 4, element)
sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" % 3, element)
sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" % 2, element)
sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" % 1.4, element)
sleep(1)

pers = []  # массив ссылок
t = 0.7  # ожидание после каждой прокрутки
num_scroll = 0  # количество совершённых прокруток
p = 0  # коэффициент ожидания

while len(pers) < full:
    num_scroll += 1
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s", element)

    if num_scroll % 10 == 0:
        print("!")
        #  сохранение пользователей
        persons = browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/span/a")
        for i in range(len(persons)):
            pers.append(str(persons[i].get_attribute('href')))
    sleep(t)

    #  ожидание
    if len(pers) > (2000 + 1000 * p):
        print("\nОжидание 10 минут")
        sleep(60 * 10)
        p += 1

#  создание файла со списком пользователей
f = open("list.txt", mode="w")
for persons in pers:
    f.write(persons)
    f.write("\n")
f.close()

# Ввод емейл
#  input_email = browser.find_element_by_name('username')
#  sleep(1)
#  sleep(1)

# Ввод пароля
#  input_email = browser.find_element_by_name('password')
#  sleep(1)
#  input_email.send_keys('glush200416')
#  sleep(1)

#  browser.find_element_by_xpath("//div[1]/div[3]").click()
# Нажатие кнопки входа
#  submit = browser.find_element_by_name('post')
#  submit.click()
#  sleep(15)
