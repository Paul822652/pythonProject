#复选框（checkbox）
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

elements = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox input[checked="checked"]')
for element in elements:
    element.click()

sleep(2)
# 再点击小雷老师
wd.find_element(By.CSS_SELECTOR, "#s_checkbox input[value='小雷老师']").click()
