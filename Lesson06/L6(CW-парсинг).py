import requests
from bs4 import BeautifulSoup

print()

url = "https://ru.wordpress.org/"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ
# my_json = site.json()
soup = BeautifulSoup(my_html, 'lxml')  # Парсим "html" методом "lxml"

temp1 = soup.find_all("header")[0]
print(temp1)
print()

temp2 = temp1.find_all("p")
print(temp2)
print()

print(temp2[0])
print(temp2[0].text)

# Одно и тоже
# p = soup.find_all("header")[0].find_all("p")[0].text
# print(p)

# !!!!!!! Задача получить текст кнопки

# lst = soup.find_all("a")
#
# c = 1
# for i in lst:
#     print(c, i)
#     c += 1

print(soup.find_all("a")[17].text)
print(soup.find_all("a")[17]['href'])

# Часть домашки

url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ
my_json = site.json()

result = None
for i in my_json:
    if i["Cur_Abbreviation"] == "USD":
        result = i["Cur_OfficialRate"]

print()
print(result)


print()
c = 1
print(my_json)
print()
for i in my_json:
    print(c, i["Cur_Name"], i["Cur_Abbreviation"], i["Cur_OfficialRate"])
    c += 1

print()
for i in my_json:
    print(i["Cur_Abbreviation"], end=" ")
