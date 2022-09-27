from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))
driver.implicitly_wait(10)
driver.get('https://cdn2.byhy.net/files/selenium/test4.html')


# --- prompt ---
driver.find_element(By.ID, 'b3').click()

# 获取 alert 对象
alert = driver.switch_to.alert

# 打印 弹出框 提示信息
print(alert.text)
sleep(5)
# 输入信息，并且点击 OK 按钮 提交
alert.send_keys('web自动化 - selenium')
alert.accept()

# 点击 Cancel 按钮 取消
driver.find_element(By.ID, 'b3').click()
alert = driver.switch_to.alert
alert.dismiss()