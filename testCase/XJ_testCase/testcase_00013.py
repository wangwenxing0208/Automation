# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 11:57 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.returnOrder import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseReturnOrder(Init,ReturnOrder,Login,Assertion):
    def test_ReturnOrder(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''退货订单是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickReturnOrder
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertequal(value, self.listReturnOrder1)

if __name__ == '__main__':
    unittest.main(verbosity=2)