# -* coding:utf-8 -*-
"""
time   :  2021/3/07 16:43
author :  zhangzhilong
effect :  测试用例
"""

from keyword_demo.base.excel import excel_keywords
from keyword_demo.conf import confs


# 关键字驱动测试
def test_login_keyword():
    # 读取Excel并执行测试
    excel_keywords().read_excel_keyword(confs.driver, confs.login_url, confs.login_path_keyword)
