# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 4:07 下午
  Author     ：star
"""

from page.login.init import *
from page.goodsCenter.goodsCategory import *
from common.login import *
from utils.assertion import Assertion

import time

class TestcaseGoodsCategory(Init,GoodsCategory,Login,Assertion):
    def test_GoodsCategory(self, value='06'):
        '''商品分类是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickGoodsCategory
        time.sleep(2)
        self.goodCategoryCode(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.self.listGoodsCategory1)

if __name__ == '__main__':
    unittest.main(verbosity=2)