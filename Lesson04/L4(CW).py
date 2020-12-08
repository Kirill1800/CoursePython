import random
from Source import fare1, fare2   # Выборочно переменные
from Source import *              # Весь файл
from termcolor import cprint

# Есть функции которые сразу доступны - range()
# Есть функции которые находятся у тебя на компьютере но доступны только после import - random()
# Есть функции которые нужно скачивать с интернета - termcolor


print(range(10))  # Создает массив с цифрами от 0 до 10

print()
print(8, end="..")
print(9)
print()

print("-------------------------------------------- Цикл FOR")

for i in range(1, 10):
    print(i, end=' ')
print()

# 1 - способ использования for
for i in range(1, 20):
    print(i)

# 2 - способ использования for
lst = ["one", "two", "three", "4", 5]
for i in lst:
    print(9)

print("-------------------------------------------- Цикл WHILE (c ПРЕДусловием)")

i = 1
while i < 10:
    print(i, end=' ')
    i += 1
print()

print("-------------------------------------------- Цикл WHILE (с ПОСТусловием)")

i = 1
while True:
    print(i, end=' ')
    i += 1
    if i >= 10:
        break
print()

print("-------------------------------------------- Цикл WHILE (бесконечный цикл)")

# 1 - бесконечный
while False:
    print("G")
    pass
    pass

# 2 - бесконечный
# num = 1
# while num < 10:
#     print("Jason Statham")

print("-------------------------------------------- True False")

val = True
while val:
    print("ooo")
    val = not val  # тоже самое: val = False
    pass  # просто заглушка

print("-------------------------------------------- Условный оператор IF-ELIF-ELSE")

count = 10
if count < 0:
    print("Число меньше нуля")
elif count > 0:
    print("Число больше нуля!")
else:
    print("Равно нулю!")

print("-------------------------------------------- Игра угадай число от 1 до 20 (5 попыток) ")

x = False
if x:
    number = random.randint(1, 20)  # Рандом от 1 до 20
    guesses = 0
    while guesses < 3:
        print('Напишите число от 1 до 20: ')
        guess = int(input())  # вводим число
        guesses += 1  # увеличиваем попытку
        if guess == number:
            print('Успех!')
            print('Вы угадали число. ' + str(guesses))
            break
        elif guess < number:
            print('Число слишком маленькое. Попробуй еще.')
        elif guess > number:
            print('Число слишком большое. Попробуй еще.')
    print('Ты не угадал число. Исходное число: ' + str(number))

print("-------------------------------------------- Вложенный цикл ")

items1 = [1, 2, 3, 4]
items2 = [6, 7, 8, 9]

for x in items1:
    print(x, end=' ')
    if x == 4:
        continue
    # При четвертой итерации первого цикла сработает continue что повлечет пропуск вложенного цикла
    for y in items2:
        print(y, end=' ')

print()
print(fare1, fare2)
cprint(str(fare1) + " " + str(fare2), "green")

cprint(str(fare1) + "" + str(fare2), "red")
