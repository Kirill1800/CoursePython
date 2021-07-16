# 1 данные 20%
# 2 условия 40%
# 3 циклы 10%


x1 = 1
x2 = "kfjfk0fkfj"
x3 = ["hdhdh", "jdujdj", 3]
x4 = {"one": 4, "two": 5}
x5 = x2 * 3

print(x5)

print(x3[1])
print(x4["two"])

# count = 0
# for i in x2:
#     print("--", count)
#     print(x2[count])
#     count += 1

print()
print()

count = 0
for j in x3:
    print(x3[count])
    count += 1

x3.append(x2)
print(x3)

x4.update({"three": x2})
print(x4)

count = 0
for k in x3:
    if isinstance(x3[count], str):
        if x3[count][0] == "j":
            print(x3[count])
    count += 1

