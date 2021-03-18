# -* coding:utf-8 -*-
"""
time   :  2021/3/07 15:17
author :  zhangzhilong
effect :  登录页面
"""

from POM_dome.base.bases import Base


class login:
    # 登录页面元素定位
    username_types = ('name', 'username')  # 账号输入框定位
    password_types = ('name', 'password')  # 密码输入框定位
    button_types = ('xpath', '//*[@id="login_form"]/div[3]/button')  # 登录按钮定位

    # 实例化时定义所需浏览器
    def __init__(self, driver):
        self.driver = driver

    # 登录
    def login(self, url, username, password):
        # 类的实例化
        driver = Base(self.driver)
        # 打开登录页
        driver.open_url(url)
        # 输入账户名
        driver.input(self.username_types, username)
        # 输入密码
        driver.input(self.password_types, password)
        # 点击登录按钮
        driver.click(self.button_types)
        # 等待一分钟，为下一次页面跳转争取时间
        driver.quit()
