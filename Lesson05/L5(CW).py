# Объявление процедуры
def func1():
    x = 5 + 7
    print(range(2, 99))
    print(str(288))
    print("Hello\n")
    print(x)


# Вызов процедуры
# func1()

# func1()

# func1()


# Отличие процедуры от функции в том, что процедура просто выполняет действия
# А функция выполняет её и ещё возвращает

# Объявление функции
def func2():
    x = 5 + 7
    print(range(2, 99))
    print(str(288))
    print("Hello")
    return x + 8  # То что функция вернёт ( то чему она будет равна )


# Вызов функции

y = func2()
print(y)


def funk3(on=False):
    if on:
        lst = []
        for i in range(10):
            lst.append(i)
        return (lst, lst)


print("Вызов 1", funk3(True))
print("Вызов 2", funk3(False))
print("Вызов 3", funk3())


def func4(x1, x2, operation):
    if operation == "+":
        return x1 + x2
    elif operation == "*":
        return x1 * x2
    else:
        return "Операция функции не известна"


class Calc:
    result = None  # Наше табло в калькуляторе

    def __init__(self, x1, x2, operation):
        if operation == "+":
            self.result = x1 + x2
        elif operation == "*":
            self.result = x1 * x2


print("Calc")
calc1 = Calc(x1=4, x2=9, operation="+")
print(calc1.result)

print("Func")
print(func4(2, 6, "+"))
print(func4(5, 3, operation="*"))
print(func4(x1=4, x2=9, operation="+"))
print(func4(x1=float(input()), x2=float(input()), operation=input()))


# Объявление процедуры


def func1():
    x = 5 + 7
    print(range(2, 99))
    print(str(228))
    print("hello\n")
    print(x)


# Вызов процедуры
# func1()

# func1()

# func1()


# Отличие процедуры от функции в том что процедура просто выполняет действия
# А функция выполняет и еще возвращает.


# Объявление функции
def func2():
    x = 5 + 7
    print(range(2, 99))
    print(str(228))
    print("hello")
    return x + 8  # То что функция вернет (то чему она будет равна)


# Вызов функции
y = func2()
print(y)
print(func2())


# Объявление функции
def func3(gap=True):  # Аргументы функции (Тут один аргумент "on" равный по умолчанию True)
    if gap:
        lst = []
        for i in range(10):
            lst.append(i)
        return [lst, lst]


print("Вызов 1", func3(True))  # Параметры True
print("Вызов 2", func3(False))
print("Вызов 3", func3())


def func4(x1, x2, operation):
    if operation == "+":
        return x1 + x2
    elif operation == "*":
        return x1 * x2
    else:
        return "Операция функции не известна!"


print()
print(func4(2, 6, "+"))
print(func4(5, 7, operation="*"))
print(func4(x1=2, x2=4, operation="+"))


# print(func4(x1=float(input()), x2=float(input()), operation=input()))


# [M] Возвращает "str" с числом "number" округленным до "n" знаков (для красивого вывода)
def okr(number, n, mode=None):
    try:
        result = str(round(number, n))  # 3.56
        ln = len(result.split(".")[1])  # 2
    except IndexError:
        result = "{:f}".format(round(number, n))  # 356.000000
        print(result)
        result = result.replace(".", ",")  # 356,000000000
        ln = len(result.split(",")[1])  # 9

    # MODE = S (Указание явно знака | минус и так показываеться, добавляем "+")
    if mode == "S":
        if not result.find("-") != -1:
            result = "+" + result

    sm = n - ln  # -4
    # Когда нехватает нулей
    if sm > 0:
        for i in range(sm):
            result += "0"
    # Когда нулей больше чем должно (сработал IndexError)
    if sm < 0:
        for i in range(abs(sm)):
            result = result[:-1]
    return result


# print(okr(number=3.56, n=3))
# print(okr(number=3.56, n=9))
# print(okr(number=3.56, n=9, mode="S"))
# print(round(3.56, 9))

print()
print()
print("#################")
print(okr(number=356, n=2, mode="S"))

print(abs(-5))

print("-------------------------------------------- Пример использования *args / **kwargs ")


# 1 Ситуация
def many(*args, **kwargs):
    print("Кортеж - ", args)
    print("Словарь -", kwargs)


many(1, 2, 3, 4, 5, name="Igor", job="Programmer", sex="Male")


# 2 Ситуация
def name(name1, name2, name3):
    print("1-ый аргумент:", name1)
    print("2-ой аргумент:", name2)
    print("3-ий аргумент:", name3)


name("Коля", "Маша", "Игорь")  # Обычная передача параметров
name(*["Коля", "Маша", "Игорь"])  # Передача параметров через массив

print("-------------------------------------------- Lambda (Мини функция)")

lam1 = lambda x, y, z: x * y + z  # Короткая запись


def lam2(x, y, z):  # Длинная запись
    return x * y + z


print("Пример Lambda (x * y + z):", lam1(2, 3, 4))
print("Пример Lambda (x * y + z):", lam2(2, 3, 4))

print("-------------------------------------------- Пример использования args*")


def many(*args):
    print(args)
    sm = 0
    for j in args[0]:
        sm += j
    return sm


lst = []
for i in range(5):
    lst.append(i)
lst = tuple(lst)  # list перевели в tuple(кортедж)

print("lst =", lst)
print("Ответ: ", many(lst))
