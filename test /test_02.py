#在股票搜索网站输入框中搜索通讯
#暂未实现，无法在已打开的浏览器中运行
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

#由于需要输入代理，所以等待10秒
sleep(10)
# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('通讯\n')