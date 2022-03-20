# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 2:11 上午
  Author     ：star
"""

from page.login.init import *
from page.settlementCenter.searchRemainMoney import *
from common.login import *
import time

class TestcaseSearchRemainMoney(Init,SearchRemainMoney,Login):
    def test_searchRemainMoney(self, value1='黑龙江飞鹤乳业销售有限公司', value2='哈尔滨迪亲商贸有限公司'):
        '''应收余额查询是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickSearchRemainMoney
        time.sleep(3)
        self.financeOrganizationName(value1)
        time.sleep(3)
        self.reconciliationDate
        time.sleep(3)
        self.customerName(value2)
        time.sleep(3)

        # self.assertEqual(self.listReceivableBill1, value1)

if __name__ == '__main__':
    unittest.main(verbosity=2)