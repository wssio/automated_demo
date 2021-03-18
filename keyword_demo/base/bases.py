# -* coding:utf-8 -*-
"""
time   :  2021/3/07 14:28
author :  zhangzhilong
effect :  基类
"""

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
        # implicitly_wait(x)浏览器隐式等待，如果定位不到则等待x秒
        self.driver.implicitly_wait(5)
        # 数据中转站
        self.transfer_data = ''

    # 进程等待
    def sleep(self, times, expectation=None, row=None):
        time.sleep(int(times))
        # 如果Excel中预期结果有数据，则执行主动断言
        if expectation != None:
            self.text_assert(expectation, row)

    # 定位元素
    def location(self, mode, element):
        # 通过id代替By.ID，自动选择定位方式
        if mode == 'name':
            return self.driver.find_element(By.NAME, element)
        elif mode == 'id':
            return self.driver.find_element(By.ID, element)
        elif mode == 'xpath':
            return self.driver.find_element(By.XPATH, element)
        elif mode == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, element)
        elif mode == 'class':
            return self.driver.find_element(By.CLASS_NAME, element)
        else:
            print("暂未定义此定位元素方式")

    # 打开网页
    def open_url(self, url):
        self.driver.get(url)

    # 文本框输入数据
    def input(self, mode, element, txt, row=None):
        try:
            # 输入前先清空此输入框，防止原有数据影响结果
            self.location(mode, element).clear()
            self.location(mode, element).send_keys(txt)
        # 如果输入过程中报错，则执行被动断言
        except Exception as e:
            self.passivity_assert(row, e)

    # 点击事件
    def click(self, mode, element, expectation=None, row=None):
        self.location(mode, element).click()
        # 如果有预期结果，则执行主动断言
        if expectation != None:
            self.text_assert(expectation, row)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 切换浏览器页面
    def handler(self, pointer, expectation=None, row=None):
        # 获取句柄值
        handlers = self.driver.window_handles
        # 切换句柄
        self.driver.switch_to.window(handlers[int(pointer)])
        # 如果Excel中预期结果有数据，则执行主动断言
        if expectation != None:
            self.text_assert(expectation, row)

    # 数据中转ctrl+c
    def ctrl_c(self, mode, element, transfer, row=None):
        try:
            self.transfer_data = self.location(mode, element).get_attribute(transfer)

        # 如果获取数据过程中报错，则执行被动断言
        except Exception as e:
            self.passivity_assert(row, e)

    # 数据中转ctrl+v
    def ctrl_v(self, mode, element, row=None):
        self.input(mode, element, self.transfer_data)

    # 主动断言:断言将异常存入日志文件
    def text_assert(self, expectation, row):
        # 拼接该文本参数的xpath
        pointer = '//*[text()="' + expectation + '"]'
        try:
            # 使用xpath方法定位元素
            self.driver.find_element(By.XPATH, pointer)
        # 如果未定位到此元素，会报NoSuchElementException错误
        except NoSuchElementException as e:
            # a为追加模式
            file = open('../log/logs.txt', 'a')
            # 写入日志文件
            file.write('【Excel第' + row + '行】    ' + time.strftime('%Y-%m-%d %H:%M:%S') + '    主动断言错误: 未在页面找[' + expectation + ']这个元素    Xpath: ' + pointer + '\n')
            # 关闭文件时数据才能写入
            file.flush()

    # 被动断言
    def passivity_assert(self, row, error):
        # a为追加模式
        file = open('../log/logs.txt', 'a')
        # 写入日志文件
        file.write('【Excel第' + row + '行】    ' + str(time.strftime('%Y-%m-%d %H:%M:%S')) + '    被动断言错误: ' + repr(error) + '\n')
        # 关闭文件时数据才能写入
        file.flush()
