#下拉框(select)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wd = webdriver.Chrome(service=Service(r'/Users/f7693194/Chrome/chromedriver'))
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

#select单选框
select = Select(wd.find_element(By.ID, "ss_single"))
select.select_by_visible_text("小雷老师")#选择小雷老师

#select多选框
select = Select(wd.find_element(By.ID, "ss_multi"))
select.deselect_all()#清除所有已经选择的选项
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
