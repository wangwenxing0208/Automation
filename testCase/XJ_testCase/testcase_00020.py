# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 8:24 下午
  Author     ：star
"""

from page.login.init import *
from page.creditCenter.creditBalanceQuery import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseCreditBalanceQuery(Init,CreditBalanceQuery,Login,Assertion):
    def test_creditBalanceQuery(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''信用余额查询是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickCreditBalanceQuery
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertequal(value, self.listCreditBalanceQuery1)

if __name__ == '__main__':
    unittest.main(verbosity=2)