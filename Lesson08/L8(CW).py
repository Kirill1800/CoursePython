import os
import random
import requests

print("-------------------------------------------- Работа с файлами")

# ---- Ш П А Р Г А Л К А ----
# r  — открывает файл только для чтения.
# w  — открывает файл только для записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи.
#      (Информация добавляеться в конец файла)


# ВАРИАНТ 1 - Запись строчки "Example" в файл "kek.txt"
file = open("kek.txt", mode="w")
file.write(str(random.randint(1, 99999)))
file.close()
os.remove("kek.txt")  # Удаление Файла "kek.txt"

# ВАРИАНТ 2 - Запись строчки "Example" в файл "kek.txt" (использоване "with" автоматически закрывает файл)
with open("kek.txt", mode="w") as file:
    file.write("Example2")
# os.remove("kek.txt")  # Удаление Файла "kek.txt"

# Чтение из файла "kek.txt"
with open("kek.txt", "r") as file:
    text = file.read(600)
    print(text)  # Читает первые 600 символов (если пропустить этот аргумент, то читает весь файл)


print("-------------------------------------------- Задание 1 (90)")

# url = 'htps://www.google.com/'  # Ошибка в URL
url = 'https://www.google.com/'  # 200
# url = 'https://www.google.com/ii'  # 404

try:
    request = requests.get(url)
    html = request.text  # Тут мы записываем содержимое сайта в html в текстовом виде (но в данном случае не используем)
    if str(request) == '<Response [404]>':
        print('Ошибочка. Сайт вернул 404!')
    if str(request) == '<Response [200]>':
        print('Гуд. Сайт вернул 200!')
except requests.exceptions.InvalidSchema:
    print('Ошибка в URL!')
except requests.exceptions.ConnectionError:
    print('Ошибка в подключении!')