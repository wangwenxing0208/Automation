# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 5:55 下午
  Author     ：star
"""

from page.login.init import *
from page.dhanneCenter.customerApply import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseCustomerApply(Init,CustomerApply,Login,Assertion):
    def test_customerApply(self, value='哈尔滨迪亲商贸有限公司'):
        '''客户申请单是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickCustomerApply
        time.sleep(2)
        self.state
        time.sleep(2)
        self.customerName(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.listCustomerApply1)

if __name__ == '__main__':
    unittest.main(verbosity=2)