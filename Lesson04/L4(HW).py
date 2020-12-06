a = b = c = 7
while a == b == c:
    print("YES")
    a += 1
    print('ERROR')
print("\nСлайд79 №2")
a = 12
b = 5
c = 17
while a + b == c:
    print("YES")
    a -= 1
    print("ERROR")
print("\nСлайд80 №1")
for i in range(1, 14):
    print(i + i)

mas = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"]
number = 1
while number < 8:
    print(number, mas)
    number += 1
    print("Конец недели")


for i in range(1, 100):
    print(i + i)
