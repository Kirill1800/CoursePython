import requests
from bs4 import BeautifulSoup


url = "https://koronavirustoday.ru/info/koronavirus-tablicza-po-stranam-mira-na-segodnya/"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ
#  my_json = site.json()
soup = BeautifulSoup(my_html, 'lxml')
temp1 = soup.find_all("div")

url = "https://meduza.io/feature/2020/03/05/poslednie-dannye-po-koronavirusu-vo-vsem-mire-tablitsa"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ
#  my_json = site.json()
#  print(my_json)

image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('new_image.png', 'wb') as f:
    f.write(image.content)
#  f.remove('new_image.png')

url = 'https://www.worldweatheronline.com/developer/login.aspx'


#  data = {"заносим сюда все ключи, которые необходимо отправить серверу в формате “key”: “value” и не забываем ставить запятые после каждого “value”"}
#  s = requests.Session()
#  s = requests.post(url)
#  my_json = s.json()
#  print(my_json)


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
    print(news.get_python_news()[2])
news_list = soup.findAll('h2', class_='post__title')
