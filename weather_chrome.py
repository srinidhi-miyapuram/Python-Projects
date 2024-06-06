
# Automate search for weather in a country

from selenium.webdriver.common.by import By
from selenium import webdriver
import time 
import random

city_list = ['New York', 'London', 'Germany', 'Hyderabad', 'Delhi', 'Switzerland', 'Australia']

rand_num = random.randint(0, len(city_list)-1)
num = random.randint(0,4)

url = "https://www.ventusky.com/"

window = webdriver.Chrome()

window.get(url)

search = window.find_element(By.ID, 'search-q')
search.send_keys(city_list[rand_num])
time.sleep(2)

city_select = window.find_element(By.TAG_NAME, 'ul')
time.sleep(2)

city = city_select.find_element(By.TAG_NAME, 'li')
time.sleep(2)

city.click()

time.sleep(20)
window.quit()
