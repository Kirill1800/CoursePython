# Класс (структура, один)
# Объект (несколько)

# Класс RGB
class Color:  # Объявление нашего класса (создание)

    # Параметры класса Color
    red = 0
    green = 0
    blue = 0

    # Инициализация класса (выполняется всегда при создании объекта)
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    # Метод(Функция) №1 класса Color (который переводит RGB переводит в 16bit)
    def to_hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)  # Штука которая из RGB переводит в 16bit

    # Метод(Функция) №2 класса Color (которая сумирует три цвета в числовом виде)
    def sum_rgb(self):
        result = self.red + self.green + self.blue
        return result


class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


gray_2 = Color(100, 100, 100)

blue = 40
obj = ColorAlpha(255, 0, 0, 0.5)  # Создаем объект red

print(ColorAlpha(255, 0, 0, 0.5))  # <__main__.ColorAlpha object at 0x7fdbc0207220>
print(ColorAlpha)  # <class '__main__.ColorAlpha'>

print(type(blue), type(obj))  # Печатаем типы данных переменных red и blue
print(obj.red, obj.green)  # Печатаем параметры класса (а именно параметры объекта red)
print(obj.to_hex())  # Печатем результат выполнения метода to.hex() для объекта red
print(obj.sum_rgb())  # Печатем результат выполнения метода sum_rgb() для объекта red

print()


# Класс Апельсинов
class Orange:

    # Инициализация класса (выполняется всегда при создании объекта)
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Наш объект создан!")


or1 = Orange(10, "Желтый")
or2 = Orange(10, "Оранжевый")
or3 = Orange(5, "Зеленый")

print(or1.color)
or1.color = "Синий"
print(or1.color)

# 41
