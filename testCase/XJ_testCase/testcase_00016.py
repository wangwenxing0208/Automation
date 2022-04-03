# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:30 上午
  Author     ：star
"""

from page.login.init import *
from page.settlementCenter.receivableBill import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseReceivableBill(Init,ReceivableBill,Login,Assertion):
    def test_ReceivableBill(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''应收单是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickReceivableBill
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertequal(value, self.listReceivableBill1)

if __name__ == '__main__':
    unittest.main(verbosity=2)