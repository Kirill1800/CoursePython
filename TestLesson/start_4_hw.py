# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Выполни 3 первые задачки (по возможности используюя функции)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for num in a:
#     if num < 5:
#         print(num)

# задача номер 1
def check_number(mas):
    for elm in mas:
        if elm < 5:
            print(elm)


print(check_number(mas=[1, 2, 3, 4, 5, 6, 7]))
print()


# задача номер 2
def double_check(mas1, mas2):
    c = []
    for i in mas1:
        for j in mas2:
            if i == j:
                flag = False
                for k in c:
                    if k == i:
                        flag = True
                if not flag:
                    c.append(i)
    return c


print(double_check(mas1=[1, 1, 1, 2, 3, 3, 5, 8, 13, 21, 34, 55, 89], mas2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print()

# задача номер 3
mas1 = [1, 90, 1, 2, 3, 3, 5, 8, 13, 21, 34, 55, 89]
print(sorted(mas1))
print(list(reversed(sorted(mas1))))


# задача номер 4
def merger(list1, list2):
    result = {}
    result.update(list1)
    result.update(list2)

    return result


print(merger(list1={"one": 1, "two": 2}, list2={"three": 3, "four": 4}))
print()


# задача номер 5
def str_to(text):
    result = text.split(",")
    return result


print(str_to("1,4,5,6,7"))
print("1,4,3,5,6".replace(",", "-"))