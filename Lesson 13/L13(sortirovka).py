from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from time import sleep


def xpath_existence(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence


#  browser = webdriver.Chrome("/Users/lawr/PycharmProjects/CoursePythonKirill/Lesson 13/chrome_driver/chromedriver_mac64")
browser = webdriver.Chrome(r"C:\Users\Admin\Documents\GitHub\CoursePython\Lesson 13\chrome_driver\chromedriver.exe")

f = open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Lesson 13\\temp.txt", 'r')
file_list = []
for line in f:
    file_list.append(line)
f.close()


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
    elm = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span"
    s = browser.find_element_by_xpath(elm).text
    if int(s.replace(" ", "")) > count:
        return True
    else:
        return False


#  3) у аккаунта не может быть больше подписчиков, чем указано
# Проверка на колличество подписок (True - если больше count, иначе False)
def check_count_subscribers(count):
    elm = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"
    s = browser.find_element_by_xpath(elm).text
    if int(s.replace(" ", "")) > int(count):
        return True
    else:
        return False


#  3) не должно быть ссылки на сайт
#  4) необходимо фото пролфиля
def chek_photo():
    elm = "/html/body/div[1]/section/main/div/header/div/div/div/button/img"
    s = browser.find_element_by_xpath(elm).get_attribute("src")
    if s.find("s150x150") == -1:
        return False
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


#  6) посленяя публикация не менее days дней назад


filter_list = []
i = 0  # подходят
j = 0  # на выходе

# Константы
days = 20
acc_subsckriptions = 200
publications = 10

# Запустим страницу
browser.get("https://www.instagram.com/accounts/login/?source=reset_password")
sleep(3)

t = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[1]/div/label/input")
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

    # Проверка
    print("Приватный? ", check_private())
    sleep(3)
    print("Больше подписок?", check_count_subscriptions(count=acc_subsckriptions))
    sleep(3)
    print("Больше подписчиков?", check_count_subscribers(count=acc_subsckriptions))
    sleep(3)
    print("Больше публикаций?", check_count_publications(count=publications))
    print("Емть аватарка?", chek_photo())

    element = "/html/body/div[1]/section/main/div/header/div/div/span/img"
    if xpath_existence(element) == 0:
        print(j, "Ошибка 4")
    status = browser.find_element_by_xpath(element).get_attribute("src")
    if status.find("s150x150") == -1:
        print("Нет аватарки")

    sleep(5)
    print()

filter_list.append(person)
print(j, "Пользователь добавлен")
i += 1

f = open("C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Lesson 13\\filtered_persons_list.txt", "w")
for line in filter_list:
    f.write(line)
f.close()
print("\nДобавлено", i, "пользователей")
