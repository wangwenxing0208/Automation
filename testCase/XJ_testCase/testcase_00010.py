# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:41 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.provincialApproval import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseProvinceApproval(Init,ProvinceApproval,Login,Assertion):
    def test_provinceApproval(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''省区审批是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickProvinceApproval
        time.sleep(2)
        self.state
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertequal(value, self.listProvinceApproval1)

if __name__ == '__main__':
    unittest.main(verbosity=2)