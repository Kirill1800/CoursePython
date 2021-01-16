import requests
from bs4 import BeautifulSoup

# --- Спарсили таблицу №1 ---

URL = "http://astro.websib.ru/sun/Astero"
site = requests.get(URL)
my_html = site.text  # Возвращает HTML ответ

soup = BeautifulSoup(my_html, 'lxml')  # Парсим "html" методом "lxml"
table1 = soup.find_all("table")[6].find_all("tbody")[0].find_all("tr")

# --- С таблицы номер 1 взяли заголовки и засунули из в массив "titles" ---

titles = []
names = table1[0].find_all("td")
for name in names:
    titles.append(name.b.text)
print(titles)


# --- С таблицы номер 1 взяли данные и засунули из в массив "result" ---

lines = table1
count = 0
result = []
for line in lines:
    if count >= 2:
        temp_lst = []
        for val in line.find_all("td"):
            temp_lst.append(val.text)
        result.append(temp_lst)
    count += 1
print(result)
