# 切换到新窗口，并在新窗口进行操作
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

mainWindow = wd.current_window_handle  # 保存当前界面的句柄
# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)

# 切回原先的网页
# 方法一：查找对应的窗口句柄，找到即切换到对应的网页
# for handle in wd.window_handles:
#     # 先切换到该窗口
#     wd.switch_to.window(handle)
#     # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
#     if '白月黑羽测试网页3' in wd.title:
#         # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
#         break
#
# print(wd.title)

# 方法二：保存需要切换的窗口句柄，当需要切换时自动切换
wd.switch_to.window(mainWindow)
print(wd.title)
