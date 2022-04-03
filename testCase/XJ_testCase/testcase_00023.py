# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:09 下午
  Author     ：star
"""

from page.login.init import *
from page.marketCastCenter.customerFlowAccount import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseCustomerFlowAccount(Init,CustomerFlowAccount,Login,Assertion):
    def test_customerFlowAccount(self, value1='黑龙江飞鹤乳业销售有限公司', value2='哈尔滨迪亲商贸有限公司'):
        '''客户费用流水账是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickCustomerFlowAccount
        time.sleep(2)
        self.organizationName(value1)
        time.sleep(2)
        self.customerName(value2)
        time.sleep(2)
        self.clickSearch
        time.sleep(10)
        self.assertequal(value1, self.listCustomerFlowAccount1)

if __name__ == '__main__':
    unittest.main(verbosity=2)