print("\nДомашняя работа слайд 25")
x = "Hello world"
print(x[0:2])
print(x[5:])
print(x * 4)
print(x[1::2])
print("\nСлайд 59")
mas1 = ["Hello", "My", "Name", "Nikita"]
print(mas1)
mas2 = [i ** 2 for i in range(1, 10)]
print(mas2)
print("\nСлайд 67")
dictionary = {"имя": " Kirill", "возраст": 16, "любимая_еда": "anything edible"}
print('My name is' + dictionary["имя"])
print("\nСлайд 76")
print("\nВведите строку")
x = input()
print(x[2])
print(x[-2])
print(x[0:5])
print(x[::2])

print(x[1::2])
print("".join(reversed(x)))  # 1
print("@", x[::-1])  # 2
print(x[::-2])
print(len(x))
