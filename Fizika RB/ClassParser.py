import requests
from bs4 import BeautifulSoup

URL = "http://astro.websib.ru/sun/Astero"
site = requests.get(URL)
my_html = site.text  # Возвращает HTML ответ
soup = BeautifulSoup(my_html, 'lxml')  # Парсим "html" методом "lxml"

# --- Спарсили таблицу №1 ---

table1 = soup.find_all("table")[6].find_all("tbody")[0].find_all("tr")

# --- Спарсили таблицу №2 ---

table2 = soup.find_all("table")[7].find_all("tbody")[0].find_all("tr")


# --- С таблицы номер 1 взяли заголовки и засунули из в массив "titles" ---


def get_titles(table):
    t = []
    names = table[0].find_all("td")
    for name in names:
        t.append(name.b.text)
    return t


titles = get_titles(table1)
# print(titles)


# --- С таблицы номер 1 взяли данные и засунули из в массив "result" ---

def get_values(table):
    count = 0
    result = []
    for line in table:
        if count >= 2:
            temp_lst = []
            for val in line.find_all("td"):
                temp_lst.append(val.text)
            result.append(temp_lst)
        count += 1
    return result


# --- Объединяем данные двух таблиц ---

values = []

for i in get_values(table1):
    values.append(i)
for i in get_values(table2):
    values.append(i)

# print(values)