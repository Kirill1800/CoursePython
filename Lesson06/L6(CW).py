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
    # Параметры класса Orange (Характеристики)
    weight = None  # Размер
    color = None  # Цвет
    state = "Не создан"  # В каком состоянии у нас апельсин

    weight = None
    color = None
    state = "Не создан"

    # Инициализация класса (выполняется всегда при создании объекта)
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.state = "Не гнилой"
        print("Наш объект создан!")

    # Метод когда апельсин гниет
    def rot(self, days):
        self.state = "Сгнил"
        # print("Апельсин сгниет через {} дней! Его цвет: {} Размер: {}".format(days, self.color, self.weight))

    def rot(self, days):
        self.state = "Сгнил"

        #  print("Апельсин сгнил через {} дней! Его цвет: {} Размер:{}".format(days, self.color, self.weight))


or1 = Orange(10, "Желтый")
or2 = Orange(10, "Оранжевый")
or3 = Orange(5, "Зеленый")
or2.rot(days=5)


or2.rot(days=5)  # Вызов метода гниения конкретно для объекта "or2"

print(or1.color)
or1.color = "Синий"
print(or1.color)
print()
print()

or4 = Orange(50, "Красный")
print(or4.state)
or4.rot(days=5)
print(or4.state)


x = [5, 6]
a = 3
b = 4.0
c = a + b
print(c)

del or2


print()
print()

or4 = Orange(50, "Красный")
print(or4.state)
or4.rot(days=5)
print(or4.state)

a = 3  # int
b = 4.0  # float
c = float(a) + b
print(c)

del or2  # Удалился объект второго апельсина

# ООП - Объектно ориентированное программирование состоит:

# ИНКАПСУЛЯЦИЯ
#   Способность сокрытии внутренних данных класса, для упрощения работы и предотвращения поломки (вмешательства извне)
#   Принцип: Используем класс без прямого доступа в его структуру.
# АБСТРАКЦИЯ
#   Способность моделирования упрощенного класса для решения конкретной проблемы.
#   Все объект и не обязательно чтобы он имел атрибуты и методы из реальной жизни.
# ПОЛИМОРФИЗМ
#   Способность создания методов (интерфейсов) которые могут обрабатывать разные типы данных (разные базовые формы).
#   Пример: print("тип строка") print(666)
# НАСЛЕДОВАНИЕ
#   Способность класса наследовать методы и атрибуты от другого класса.
#   Родительский класс - класс от которого наследуем. Дочерний класс - класс который наследует.
#   Множественное наследование - это наследование от нескольких родительских классов.
#   Дочерний класс не затрагивает родительский.
