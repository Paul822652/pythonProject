from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))

wd.get('http://10.141.6.81:8081/#/login')

element = wd.find_element(By.CSS_SELECTOR, '[name="username"]')
element.send_keys('admin')#指定输入框内输入admin

element1 = wd.find_element(By.CSS_SELECTOR, '[name="password"]')
element1.send_keys('admin')#指定输入框内输入admin

element2 = wd.find_element(By.CSS_SELECTOR, '[type="button"]')
element2.click()#模拟鼠标左键单击



