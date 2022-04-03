# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 4:22 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.allowSaleGoods import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseAllowSaleGoods(Init,AllowSaleGoods,Login,Assertion):
    def test_allowSaleGoods(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''允销目录是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickAllowSaleGoods
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.listAllowSaleGoods1)

if __name__ == '__main__':
    unittest.main(verbosity=2)