from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)

time.sleep(5)

elements=browser.find_elements(By.CSS_SELECTOR, '.content')

for element in elements:
    print("****************")
    print(element.text)

browser.close()

