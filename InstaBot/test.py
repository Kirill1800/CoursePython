from selenium.webdriver.chrome.options import Options
import json
from InstaBot.path import path_top
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
from InstaBot.path import path_web_driver, path_top_10

# https://stackoverflow.com/questions/65443542/why-doesnt-instagram-work-with-selenium-headless-chrome

#
chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# browser = webdriver.Chrome(path_web_driver, options=chrome_options)
#
# browser.get("https://google.com")
#
# print(browser.find_element_by_xpath("/html").text)

chrome_options.add_argument("--window-size=1000,1080")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Chrome(path_web_driver, options=chrome_options)
browser.get("https://www.instagram.com")
sleep(5)
# browser.refresh()
browser.get_screenshot_as_file(f"screenshot.png")
