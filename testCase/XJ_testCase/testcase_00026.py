# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:39 下午
  Author     ：star
"""

from page.login.init import *
from page.planCenter.areaPlan import *
from common.login import *
import time

class TestcaseAreaPlan(Init,AreaPlan,Login):
    def test_areaPlan(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''客户要货计划是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickAreaPlan
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(10)
        self.assertEqual(self.listAreaPlan1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)