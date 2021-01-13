import requests
from bs4 import BeautifulSoup


# Сайт состоит
# 1. Внутренности сайта (PHP, Python) [Backend - скрытый слой]
# 2. Внешний вид сайта (HTML, CSS, JS) [Frontend - явный слой]
#  2.1 HTML - Разметка сайта (основа всегда виден)
#  2.1 CSS - Таблица стилей (цвет, размер, фон)
#  2.1 JS - Для динамики сайта

url = "https://koronavirustoday.ru/info/koronavirus-tablicza-po-stranam-mira-na-segodnya/"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ (всегда)
# my_json = site.json()  # Он есть только когда у сайта есть свой API (не всегда)
soup = BeautifulSoup(my_html, 'lxml')

names = []
count = 0
for i in soup.find_all("div", "item"):
    count += 1
    if count <= 4:
        names.append(i.text.split("\n")[1].replace("\t", ""))
    else:
        pass

print(names)

temp1 = soup.find_all("span", "big olivedrab")[0].text
temp2 = soup.find_all("span", "big red")[0].text
temp3 = soup.find_all("span", "big green")[0].text
temp4 = soup.find_all("span", "big dodgerblue")[0].text
values = [temp1, temp2, temp3, temp4]

print()
for i in range(4):
    print(names[i] + " - " + values[i])
print()

# Сохранение картинки
image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('../new_image.png', 'wb') as f:
    f.write(image.content)
#  f.remove('new_image.png')



class HabrPythonNews:

    def __init__(self):
        self.url = 'https://habr.com/ru/hub/python/'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll('h2', class_='post__title')
        return news_list


if __name__ == "__main__":
    news = HabrPythonNews()
    print(news.get_python_news()[0].a.text)
news_list = soup.findAll('h2', class_='post__title')
