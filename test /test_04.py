from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')

#由于需要输入代理，所以等待15秒
sleep(20)

element = wd.find_element(By.ID, "input1")

element.clear() # 清除输入框已有的字符串
sleep(3)
element.send_keys('白月黑羽') # 输入新字符串