from datetime import datetime
from datetime import timedelta
import random
import os

d = timedelta(hours=4)
print(d)

t = datetime.now()
print(str(t))
print(t)
print(t - d)
print(t - timedelta(days=365))
result = t - timedelta(days=365)
result = str(result)
print(result)
e = datetime.strptime(result[0:19], '%Y-%m-%d %H:%M:%S')
print(e - timedelta(days=365))
# --------------- random ---------------
print(random.randint(1, 30))
print(random.random())
print(random.uniform(100, 1000))

# --------------- os ---------------

absolute_pathe = "C:\\Users\\Admin\\Documents\\GitHub\\CoursePython\\Lesson09"
name_folder = "NewDir"
try:
    os.mkdir(absolute_pathe + "\\" + name_folder)
except FileExistsError:
    os.rmdir(absolute_pathe + "\\" + name_folder)  # Удаление папки
#  Создание файла
with open(absolute_pathe + "\\" + "name_file", "a+") as file:
    file.write(" temp temp temp")

# Переменование папки
os.rename("name_file", "edit")
