import requests
from bs4 import BeautifulSoup

url = "https://sites.google.com/view/matema-bot/6-класс/рациональные-числа/тема-21-модуль-числа-противоположные-числа-множество-целых-чисел"
url = "https://sites.google.com/view/matema-bot/6-класс/рациональные-числа/тема-22-сравнение-рациональных-чисел"
site = requests.get(url)
my_html = site.text  # Возвращает HTML ответ (всегда)
# my_json = site.json()  # Он есть только когда у сайта есть свой API (не всегда)
soup = BeautifulSoup(my_html, 'lxml')

# url_video = soup.find_all("iframe")


# print(url_video)
print(soup)