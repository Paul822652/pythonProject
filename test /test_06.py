from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))

wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')

sleep(15)

elements = wd.find_elements(By.CSS_SELECTOR, '#t1>span,#t1>p')
for element in elements:
    print(element.text)