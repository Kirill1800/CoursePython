import requests
from bs4 import BeautifulSoup
URL = "http://astro.websib.ru/sun/Astero"
site = requests.get(URL)
my_html = site.text  # Возвращает HTML ответ
#  print(my_html)
#  my_json = site.json()
soup = BeautifulSoup(my_html, 'lxml')  # Парсим "html" методом "lxml"
temp1 = soup.find_all("tr")
print(temp1[2].text)
