from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))

# 调用WebDriver对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
