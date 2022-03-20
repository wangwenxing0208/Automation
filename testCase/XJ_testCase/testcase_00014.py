# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 12:28 上午
  Author     ：star
"""

from page.login.init import *
from page.stockCenter.sale0ut0rder import *
from common.login import *
import time

class TestcaseSaleOutOrder(Init,SaleOutOrder,Login):
    def test_saleOutOrder(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''销售出库是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickSaleOutOrder
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertEqual(self.listSaleOutOrder1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)