# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:35 上午
  Author     ：star
"""

from page.login.init import *
from page.settlementCenter.gatheringBill import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseGatheringBill(Init,GatheringBill,Login,Assertion):
    def test_GatheringBill(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''收款单是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickGatheringBill
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertequal(value, self.listGatheringBill1)

if __name__ == '__main__':
    unittest.main(verbosity=2)