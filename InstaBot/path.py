import os


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


# Main (Формируем основные пути к файлам)
if get_os()[1] == "Windows":
    path_source = "C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\InstaBot\\"
    path_web_driver = path_source + "chrome_driver\chromedriver.exe"
else:
    path_source = "/Users/kirillglusakov/Documents/GitHub/CoursePython/InstaBot/"
    path_web_driver = path_source + "chrome_driver/chromedriver"

path_users = path_source + "users_url.txt"
path_sort = path_source + "users_sort.txt"
path_subscriptions = path_source + "users_sub.txt"
path_top = path_source + "users_top.json"
