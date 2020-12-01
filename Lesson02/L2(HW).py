# - вызываем ошибки
print("\nError 1")
try:
    print(int("Привет мир!"))
except ValueError:
    print("Была ошибка")

print("\nError 2\n")
try:
    print(a)
except NameError:
    print("Была ошибка")


print("\nError 3")
try:
    a = 8
    b = 10
    c = a * b
    print(c)
except SyntaxError:
    print("Была ошибка")
print("\nError 4")


