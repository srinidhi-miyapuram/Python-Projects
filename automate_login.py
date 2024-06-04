
# Automate login

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "<Enter the url here>"
username = "username"
password = "Password!"

driver = webdriver.Chrome()
driver.get(url)
search = driver.find_element(By.ID, 'username')
search.send_keys(username)
psearch = driver.find_element(By.NAME, 'password')
psearch.send_keys(password)
bsearch = driver.find_element(By.TAG_NAME, 'button')
bsearch.click()
time.sleep(10)
driver.quit()