# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 8:41 下午
  Author     ：star
"""

from page.login.init import *
from page.creditCenter.creditRecalcula import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseCreditRecalcula(Init,CreditRecalcula,Login,Assertion):
    def test_creditRecalcula(self, value1='销售公司信用控制策略', value2='哈尔滨迪亲商贸有限公司'):
        '''信用占用重算是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickCreditRecalcula
        time.sleep(3)
        self.controlStrategy(value1)
        time.sleep(3)
        self.customerName(value2)
        time.sleep(10)
        self.clickCreditRecalcula
        self.asserteual(value1, self.listCreditRecalcula1)

if __name__ == '__main__':
    unittest.main(verbosity=2)