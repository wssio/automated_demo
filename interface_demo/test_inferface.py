# -* coding:utf-8 -*-
"""
time   :  2021/3/09 13:52
author :  zhangzhilong
effect :  接口测试类
"""

import re
import time
import requests
import pytest

# 可封装为 配置项/参数化
url_login = 'http://www.baidu.com'
url_new_class = 'http://www.baidu.com'

# 参数化
data_login = {
    'username': '17688888888',
    'password': '88888888888',
}

# 创建教室所需数据
data_new_class = {
    'title': '17688888888',
    'startTime': time.strftime('%Y-%m-%d %H:%M'),
    'courseLength': '3',
    'courseType': '2',
    'video': 'on',
    'audienceCount': '0'
}


def test_interface_001():
    # .session()方法可以记录请求头
    session = requests.session()
    # 调用post请求登录网站
    session.post(url_login, data=data_login)
    # 调用get请求切换到创建教室页面
    new_class = session.get(url_new_class)
    # 在创建教室页面中调用.findall方法利用正则表达式获取token
    token = re.findall('name="token" value="(.*?)"', new_class.content.decode('utf-8'), re.S)
    # 将token传入data_new_class
    data_new_class['token'] = str(token[0])
    # 创建课程
    administrator = session.post(url_new_class, data_new_class)
    # 获取老师邀请码并打印
    teacher_url = re.findall('<span class="login_code">邀请码：(.*?)</span>', administrator.content.decode('utf-8'), re.S)
    # 获取教室roomId
    student_url = re.findall('当前邀请人数：<a href="/jiangzuo/(.*?)/code"', administrator.content.decode('utf-8'), re.S)
    print('老师邀请码:' + teacher_url[0])
    print('roomId:' + student_url[0])


if __name__ == '__main__':
    # '-v'显示运行函数 '-s'打印print
    pytest.main(['-v', '-s'])
