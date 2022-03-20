# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:57 下午
  Author     ：star
"""

from page.login.init import *
from page.B2BOrderCenter.orderReview import *
from common.login import *
import time

class TestcaseOrderReview(Init,OrderReview,Login):
    def test_orderReview(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''订单财审是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickOrderReview
        time.sleep(2)
        self.state
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertEqual(self.listOrderReview1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)