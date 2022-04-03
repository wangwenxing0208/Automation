# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:22 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.saleOrder import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseSaleOrder(Init,SaleOrder,Login,Assertion):
    def test_saleOrder(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''销售订单是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickSaleOrder
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.listSaleOrder1)

if __name__ == '__main__':
    unittest.main(verbosity=2)