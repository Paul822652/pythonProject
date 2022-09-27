# 鼠标移动到某个元素
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))
wd.implicitly_wait(15)

wd.get('https://www.baidu.com/')

ac = ActionChains(wd)

# 鼠标移动到 元素上
ac.move_to_element(
    wd.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')
).perform()

sleep(3)

wd.find_element(By.CSS_SELECTOR, '[name="tj_fanyi"]').click()
