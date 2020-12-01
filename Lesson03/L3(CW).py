print("\n***Множественное присвайвание:")

a = b = c = 5
print(a, b, c)

print("\n***Разбираем строки:")

string = "Hello"

print(string[0])
print(string[-1])

print("\n***Элементарный цикл for где пробегаем по каждому символу и выводим его:")

for x in string:
    print(x)

print("\n***Срезы:")

print(string[1:4])  # ell
print(string[1:])  # ello
print(string * 2)  # HelloHello

print("\n***Массив (лист):")

mas1 = [5, 6, 7]
mas2 = ['Hello', 'My', "Name", "Nikita"]

print(mas1)
print(mas2[-1])

print("\n***Булевый тип:")

x = True
y = False
z = not x

print(x, y, z)

# Одно и тоже
x = False
if x == True:
    print("1")
if x == False:
    print("2")

# Одно и тоже
x = False
if x:
    print("1")
if not x:
    print("2")

# Одно и тоже
x = 1
if x == 0:
    print("1")
if x == 1:
    print("2")

print("\n***Изменение массива:")
mas2 = ['Hello', 'My', "Name", "Nikita"]
print(mas2)
mas2[3] = "Igor"
print(mas2)
mas2[3] = 5
print(mas2)
mas2[2] = True
print(mas2)

print("\n***Виды массивов:")
var1 = [5, 6]  # Лист(Список)
var2 = {"Ящик1": 5, "Ящик2": 6}  # Словарь
var3 = (5, 6)  # Кортеж

print(var1, var2, var3)

# Задание - Хотим получить чифру 6
print(var1[1])
print(var2["Ящик2"])

print("\n***Тема: переменная и ссылка на переменную:")
# Создаем
list1 = [5, 6]
list2 = [7, 8]
# Печатаем
print(list1, list2)
# Изменяем
list1[0] = 8
# Снова печатаем
print(list1, list2)
# Присвайваем (тобишь даем ссылку на list2 в переменную list1)
list1 = list2
# Снова печатаем
print(list1, list2)
# Изменим только list2
list2[1] = 0
# Снова печатаем
print(list1, list2)  # Тут измениться и list1 (так как он ссылается на list2)

print("\n***Методы(Функции) списков(словарей):")
list1 = [5, 6]
print(list1)
list1.append(7)
print(list1)
list1.reverse()
print(list1)
list1.clear()
print(list1)

print("\n***Сортировка значений в массиве:")
list2 = [5, 6, 1, 0, 9, 11]
print(list2)
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)

print("\n**Функция dict():")
var1 = ["Ящик1", 4]
var2 = ["Ящик2", 5]
var3 = dict([var1, var2])
print(var3)

print("\n**Функция get():")
var2 = {"Ящик1": 5, "Ящик2": 6}
print(var2.get("Ящик1"))  # одно и тоже
print(var2["Ящик1"])      # одно и тоже
print("\nМножественное присваивание")
a = b = c = 5
print(a, b, c)

print("\nРазбираем строки")
str()
string = "Hello"

print(string[0])
print(string[-1])

print("\nЭллементарный цикл, пробегаем по каждому символу")
for i in string:
    print(i)

print("\nСрезы")
print(string[1:4])  # ell в срезе считается не с 0
print(string[1:])  # ello
print(string * 2)  # HelloHello

print("\nМассив лист")
mas1 = [5, 6, 7]  # лист
mas2 = ["Hello", "My", "Name", "Nikita"]

print(mas1)
print(mas2[-1])

print("\nБулевой тип")

x = True
y = False
z = not x

print(x, y, z)
# одно и тоже
x = False
if x == True:
    print(1)
if x == False:
    print(2)

x = False
if x:
    print(1)
if not x:
    print(2)

x = 0
if x == 0:
    print(1)
if not x == 1:
    print(2)

print("\nИзменение массива")
mas2 = ["Hello", "My", "Name", "Nikita"]
print(mas2)
mas2[3] = "Igor"
print(mas2)
mas2[3] = 5
print(mas2)
mas2[2] = True
print(mas2)

print("\nВиды массивов")
var1 = [5, 6]  # лист(Список)
var2 = {"Ящик": 5, "Ящик2": 6}  # словарь
var3 = (5, 6)  # кортеж

print(var1, var2, var3)
# хотим получить цифру 6
print(var1[1])
print(var2["Ящик"])

print("\nТема : переменная и ссылка на переменную")
# Создаём
list1 = [5, 6]
list2 = [7, 8]
# Печатаем
print(list1, list2)
# Изменяем
list1[0] = 8
# Печатаем
print(list1, list2)
# Присваеваем (тобишь даём ссылку на list2  в переменную list1)
list1 = list2
# Печатаем
print(list1, list2)
# Изменяем только list2
list2[1] = 0
# Печатаем
print(list1, list2)  # Тут изменится и ist1 (так как он ссылается на list2)

print("\nМетоды(Функции) списков(словарей)")
list1 = [5, 6]
print(list1)
list1.append(7)  # добавление элемента в список
print(list1)
list1.reverse()
print(list1)
list1.clear()
print(list1)
list1.insert(0, 3)
print(list1)

print("\nСортировка значений в массиве")
list2 = [5, 6, 1, 0, 9, 11]
print(list2)
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)

print("\nФункция dict()")
var1 = ["Ящик1", 4]
var2 = ["Ящик2", 5]
var3 = dict([var1, var2])
print(var3)

print("\nФункция get()")
var2 = {"Ящик": 5, "Ящик2": 6}
print(var2.get("Ящик"))





print("-------------------------------------------- Срезы")

a = b = my_str = 'Hello World!'  # Множественное присвоение

print(my_str)  # Hello World!                   # ИСХОДНАЯ
print(my_str[0])  # H                              # Первый элемент
print(my_str[-1])  # !                              # Последний элемент
print(my_str[2:5])  # llo                            # Срез (от:до)
print(my_str[2:])  # llo World!                     # Срез (от:до)
print(my_str[0::2])  # HloWrd                         # С нулевого символа с шагом 2
print(my_str[::-1])  # !dlroW olleH                  # Перевернуть строку
print(my_str * 2)  # Hello World!Hello World!       # Дублирование строки
print("Количество символов: " + str(len(my_str)))  # Длина строки

print("-------------------------------------------- Метод format()")

# 1 Вариант
print("Бла{}, Бла{}, Бла{}, Бла{}".format(1, 2, 3, 4))
# 2 Вариант
text = "Бла{}, Бла{}, Бла{}, Бла{}"
formats = text.format(1, 2, 3, 4)
print(formats)
# 3 Вариант
print("Бла{num1}, Бла{num2}, Бла{num3}, Бла{num4}".format(num1=1, num2=2, num3=3, num4=4))

print("-------------------------------------------- Кортеж")

# Пустой кортеж
ktg0 = tuple()
ktg1 = ()
print('Пустые кортежи: ')
print(ktg0)
print(ktg1)

# Заполненный кортеж
string = "Python"
ktg2 = (string[0], string[1], string[2], string[3], string[4], string[5])
print('Заполненный кортеж: ')
print(ktg2)

# Кортеж из 1-го элемента
ktg3 = ('example',)
print('Кортеж из 1-го элемента: ')
print(ktg3)

print("-------------------------------------------- Список")

# Пустой список
sps1 = list()
sps2 = []
print('Пустые списки: ')
print(sps1)
print(sps2)

# Заполненный список
string = "Python"
sps3 = [string[0], string[1], string[2], string[3], string[4], string[5]]
print('Заполненный список: ')
print(sps3)

# Разница при присваивании
print('Разница при присваивании (смотреть код):')
sps4 = list(sps3)  # 1 способ
sps5 = sps3  # 2 способ
print(sps4, sps5)  # ['P', 'y', 't', 'h', 'o', 'n'] ['P', 'y', 't', 'h', 'o', 'n']
sps3[2] = [1, 2, 3, 4, 5, 6]  # ПРИ ИЗМЕНЕНИИ В sps3 РЕЗУЛЬТАТ СКАЗЫВАЕТСЯ НА sp5
print(sps4, sps5)  # ['P', 'y', 't', 'h', 'o', 'n'] ['P', 'y', [1, 2, 3, 4, 5, 6], 'h', 'o', 'n']
sps3 = [1, 2, 3, 4, 5, 6]  # НЕ ВЛИЯЕТ
print(sps4, sps5)  # ['P', 'y', 't', 'h', 'o', 'n'] ['P', 'y', [1, 2, 3, 4, 5, 6], 'h', 'o', 'n']

# Методы списков
print('Методы списков:')
sps6 = [1, 2]
print('Исходный список = ' + str(sps6))
# Метод "extend" ДобавлениеЭлементов/СлияниеСписков
sps6.extend(sps6)
print('sps6.extend(sps6) = ' + str(sps6))
# Метод "append" ДобавлениеОдногоЭлемента
sps6.append(13)
print('sps6.append(13)  = ' + str(sps6))
# Метод "insert" ВставитьЭлементВПозицию
sps6.insert(0, 9)
print('sps6.insert(0,9) = ' + str(sps6))
# Метод "remove" УдалениеПервогоВведенногоЭлемента
sps6.remove(2)
print('sps6.remove(2)   = ' + str(sps6))
# Не Метод "del" УдалениеПоИндексу
del sps6[3]
print('del sps6[3]      = ' + str(sps6))
# Метод "reverse" МеняеПпорядокСпискаНаОбратный
sps6.reverse()
print('sps6.reverse()   = ' + str(sps6))

# Сортировка списка
print('Метод sorted():')
sps7 = [[1, 2, 3, 4], [2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4, 5], [10], [2, -100], [1, 3, 2, 4], [1, 2, 3, 4]]
print(sps7)
print(sorted(sps7))

print("-------------------------------------------- Генератор Списка")

# Формирует список из "i" которая в цикле принимает каждую букву в слове "loshadka"
gen_a = [i for i in "loshadka"]
print(gen_a, "- [i for i in \"loshadka\"]")

# Формирует список из "i*3" которая в цикле принимает от 1 до 10
gen_b = [i * 3 for i in range(1, 10)]
print(gen_b, "- [i * 3 for i in range(1, 10)]")

# Формирует список из "i*2" которая в цикле принимает каждую букву в слове "Igor" кроме символа "I"
gen_c = [i * 2 for i in "Igor" if i != 'I']
print(gen_c, "- [i * 2 for i in \"Igor\" if i != 'I']")

print("-------------------------------------------- Словарь")

# Создание словаря и вывод значения по ключу
dic_a = {"name": 'Игорь', "age": '22', "sex": 'Мужской'}
print(dic_a)
print(dic_a["sex"])

# Генерация словаря из двумерного списка
# dic_b = [[1, 2], [2, 4], [3, 9], [4, 16]]  # Ключ - значение, данные - квадрат значений
# dic_c = dict(dic_b)
# print("КЛЮЧ - значение, ДАННЫЕ - квадрат значений:", dic_с)

# Методы словарей
print("Метод 'dict.fromkeys': ", dict.fromkeys(["a", "b", "c"], 666), " - присвайвает одинаковые значения.")
# Возвращает данные по ключу, если данных нет, то будет не ошибка, а альтенативное значение.
print("Метод 'dict.get': ", dic_a.get('Яблоко', 'Ошибка'), "(Альтернативное),", dic_a.get('name', 'Ошибка'),
      "(Правильное)")

