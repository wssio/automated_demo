# -* coding:utf-8 -*-
"""
time   :  2021/3/07 16:43
author :  zhangzhilong
effect :  测试用例
"""

import pytest

from POM_dome.base.excel import excel
from POM_dome.conf import confs
from POM_dome.page_object.login import login


# 数据驱动
@pytest.mark.parametrize('number,title,username,password', excel.read_excel(confs.login_path))
# 测试登录页
def test_login_001(number, title, username, password):
    # 实例化
    login_page = login(confs.driver)
    # 调用登录页面
    login_page.login(confs.login_url, username, password)
