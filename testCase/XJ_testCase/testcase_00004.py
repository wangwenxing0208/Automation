# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 4:37 下午
  Author     ：star
"""

from page.login.init import *
from page.dhanneCenter.customer import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseCustomer(Init, Customer, Login, Assert):
    def test_customer(self, value='232004'):
        '''客户档案是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickCustomer
        time.sleep(2)
        self.customerCode(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.listCustomer1)

if __name__ == '__main__':
    unittest.main(verbosity=2)