import requests
from bs4 import BeautifulSoup

URL = "https://sites.google.com/u/0/d/1auJtYpLlqNs3fX1cJiZQR-ImIt2pDhKM/p/1R7fqbQVmvLJGrmMUsFMyTOygwUlTqIe7/preview?authuser=0"
site = requests.get(URL)
my_html = site.text  # Возвращает HTML ответ
soup = BeautifulSoup(my_html, 'lxml')  # Парсим "html" методом "lxml"
print(my_html)

