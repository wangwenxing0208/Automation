# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:47 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.headquartersApproval import *
from common.login import *
import time

class TestcaseHeadquartersApproval(Init,HeadquartersApproval,Login):
    def test_headquartersApproval(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''总部审批是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickHeadquartersApproval
        time.sleep(2)
        self.state
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertEqual(self.listHeadquartersApproval1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)