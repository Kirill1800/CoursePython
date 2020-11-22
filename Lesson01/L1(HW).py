print("\nВведите первое число")
x = float(input())
print("\nВведите знак операции")
z = input()
print("\nВведите второе число")
y = float(input())
if z == '+':
    print(x + y)
if z == '-':
    print(x - y)
if z == '*':
    print(x * y)
if z == '/' and y == 0.0:
    print("Делить на ноль нельзя!")
else:
    print(x / y)
if z == '**':
    print(x ** y)
if z == '//' and y == 0.0:
    print("Делить на ноль нельзя!")
else:
    print(x // y)
if z == '%':
    print(x % y)
