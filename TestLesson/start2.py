#  Суммирование
def summation(x1, x2):
    result = x1 + x2
    return result


# Умножение
def multiplication(x1, x2):
    result = x1 * x2
    return result


# Разность
def difference(x1, x2):
    result = x1 - x2
    return result


# Калькулятор производит операцию "sign" с числами "x1" и "x2"
def calc(x1, x2, sign):
    result = "Операции не существует 1"
    if sign == "+":
        result = summation(x1, x2)
    elif sign == "*":
        result = multiplication(x1, x2)
    elif sign == "-":
        result = difference(x1, x2)
    return result


# Поиск символа в строке (на низком уровне)
def check_symbol(string, symbol):
    result = None

    for i in string:
        if i == symbol:
            result = True
            break
        else:
            result = False

    return result


# Поиск символа в строке (на высоком уровне)
def check_symbol_2(string, symbol):
    result = string.find(symbol)
    if result == -1:
        return False
    else:
        return True


# Возвращаем текст из файла
def read_text_on_the_file(file):
    result = None
    path = "/Users/kirillglusakov/Documents/GitHub/CoursePython/TestLesson/" + file
    with open(path, 'r') as abracadabra:
        result = abracadabra.read()
    return result


print(summation(summation(180, 10), 6))
print(multiplication(16, 10))
# print(difference(int(input()), 5))

print()
print("Ответ:", calc(5, 5, "+"))
print(calc(5, 10, "*"))
print(calc(5, 5, "-"))
print(calc(10, 15, "/"))

print("Есть ли в строке символ:", check_symbol(string="Привет", symbol="в"))
print("Есть ли в строке символ:", check_symbol("Привет", "к"))

print("Есть ли в строке символ:", check_symbol_2("Привет", "в"))

print()

print("Текст из файла: \n",  read_text_on_the_file(file="start.py"))
print("Текст из файла: \n",  read_text_on_the_file(file="start2.py"))
