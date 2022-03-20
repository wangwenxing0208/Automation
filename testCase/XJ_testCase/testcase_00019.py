# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 9:33 上午
  Author     ：star
"""

from page.login.init import *
from page.promotionCenter.promotionActivity import *
from common.login import *
import time

class TestcasePromotionActivity(Init,PromotionActivity,Login):
    def test_promotionActivity(self, value='黑龙江飞鹤乳业销售有限公司'):
        '''促销活动是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickPromotionActivity
        time.sleep(2)
        self.organizationName(value)
        time.sleep(2)
        self.clickSearch
        self.assertEqual(self.listPromotionActivity1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)