# a = b = c = 7
# while a == b == c:
#     print("YES")
#     a += 1
#     print('ERROR')
#
#
#
# print("\nСлайд79 №2")
# a = 10
# b = 20
# c = 10
#
# flag = False
# for i in range(2):
#     if i == 0:
#         if a + b == c:
#             flag = True
#     if i == 1:
#         if a + c == b:
#             flag = True
#
# if flag:
#     print("YES")
# else:
#     print("ERROR")


# print("\nСлайд80 №1")
# for i in range(1, 14):
# print(i + i)


mas = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"]
number = 1
while number < 8:
    print(number, mas)
    number += 1
    print("Конец недели")

for i in range(1, 10):
    print(i)

import random

number = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)]
print("Исходные числа", number)

flag = False
for i in [0, 1]:
    for j in [1 + i, 2]:
        if number[i] == number[j]:
            flag = True
            break
if flag:
    print("YES")
else:
    print("ERROR")

flag = False
for i in range(2):
    if i == 0:
        if a + b == c:
            flag = True
    if i == 1:
        if a + c == b:
            flag = True
if flag:
    print("YES")
else:
    print("ERROR")

# 81
number = [i for i in range(15)]
print(number)
result = number[0]
print("Исходные числа: ", number)
count = 1
for i in range(1, 15):
    pre_result = result
    result = result + number[i]
    # print("Итерация №" + str(count) + " result=" + str(result))
    print("Итерация №{} result={} ({}+{})".format(count, result, pre_result, number[i]))
    count += 1
print("Сумма чисел: ", result)

print("Hello", 5)
print("Hello" + str(5))
print("Hello {}".format(5))

# 81 4
index = 0
days = ["Понедельник", "Вторник", "Седа", "Четверг", "Пятница", "Суббота", "Воскресенье"]
for i in days:
    if (index == 5) or (index == 6):
        print(days[index], index + 1, "число", "(Выходной)")
    else:
        print(days[index], index + 1, "число")
    index += 1
