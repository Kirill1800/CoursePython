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
