# -* coding:utf-8 -*-
"""
time   :  2021/3/07 14:28
author :  zhangzhilong
effect :  基类
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class Base:
    # 构造函数选择浏览器驱动
    def __init__(self, driver):
        if driver == "Chrome":
            self.driver = webdriver.Chrome()
        elif driver == "Firefox":
            self.driver = webdriver.Firefox()
        elif driver == "Ie":
            self.driver = webdriver.Ie()
        else:
            print("暂未定义此浏览器驱动")

    # 定位元素
    def location(self, types):
        # 通过id代替By.ID，自动选择定位方式
        if types[0] == 'name':
            return self.driver.find_element(By.NAME, types[1])
        elif types[0] == 'id':
            return self.driver.find_element(By.ID, types[1])
        elif types[0] == 'xpath':
            return self.driver.find_element(By.XPATH, types[1])
        elif types[0] == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, types[1])
        elif types[0] == 'class_name':
            return self.driver.find_element(By.CLASS_NAME, types[1])
        else:
            print("暂未定义此定位元素方式")

    # 打开网页
    def open_url(self, url):
        self.driver.get(url)

    # 文本框输入数据
    def input(self, types, txt):
        self.location(types).send_keys(txt)

    # 点击事件
    def click(self, types):
        self.location(types).click()
    # 退出浏览器
    def quit(self):
        self.driver.quit()
