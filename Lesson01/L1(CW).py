print("*** Тут печатаем просто текст")

print("Hello world!")

text = "Hello world!"
print(text)

print("\n***Тут используем символновой строки")
print("H\ne\nl\nl\no")

print("\n*** Тут пресваеваем переменным разные типы данных")
var1 = 5  # (int)
var2 = "ПриветМир"  # (str)
var3 = 5.5  # (float)
var4 = [var1, var2, var3]  # лист
var5 = {"Какие-то данные": var1, "Какие-то данные 2": var2}  # (dict)

print("\n***Тут используем комментарии")
# var6 = 6
'''
Второй тип коментария
var7 = 7
(Переменная var5 и var6 питон не увидит)
'''
print("\n***Тут тут выводим значение переменных")
print(var1, var2, var3, var4, var5)

# Функции
print("Наши переменные:")  # - Функция печати
# type(None)  # - это функция которая возвращает тип переменной
# len(None)  # - ЭТО Функция возвращает длину переменной
# str() int() float()  # - это Функция меняет тип
# input()  # - это Функция которая принимает значение с клавиатуры


print("\n***Тут выводим тип переменных")
print(type(var1), type(var2), type(var3), type(var4), type(var5))

print("\n***Тут выводим словарь")
print(var5["Какие-то данные"])
print(var5["Какие-то данные 2"])
print()

# Стили которых нужно придерживаться в названии переменных и функций
my_name = "Kirill"
MyName = "kirill"

print("\n***Тут меняем переменную")
var1 = 6
print(var1)

var1 = var2
print(var1)

var1 = None
print(var1)

print("\n***Тут Инкрементируем и Декрементируем")
var1 = 1
var1 += 1  # Инкрементировать
var1 += 2
var1 += 3
var1 -= 1  # Декрементировать
print(var1)

print("\n***Тут выводим длину строки")
print(var2, len(var2))

print()
print("\nИзменение типов данных:")
value1 = str(5) + "ПриветМир"
value2 = int("7") + 7
print(value1, value2)

print("\nПишем калькулятор сложения X и Y:")
print("Введите число x")
x = int(input())
print("Введите число y")
y = int(input())
z = x + y
print("Результат", z)

if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '*':
    print(x * y)
elif z == '/':
    if y == 0.0:
        print("На ноль делить нельзя!")
    else:
        print(x / y)
elif z == '**':
    print(x ** y)
elif z == '//':
    if y == 0.0:
        print("На ноль делить нельзя!")
    else:
        print(x // y)
elif z == '%':
    print(x % y)
else:
    print("Операции не существует")

# - if
# - if - else
# - if - elif- else


a = 1
b = 2
temp = a  # сохраняем первую а
a = b  # 2 меняем А на В
b = temp  # Записываем в В сохраненное первое значение А
print(a, b)  # 2, 1
