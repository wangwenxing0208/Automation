# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 8:54 下午
  Author     ：star
"""

from page.login.init import *
from page.goodsCenter.goods import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseGoods(Init,Goods,Login,Assertion):
    def test_Goods(self, value='10081038'):
        '''商品是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickGoods
        time.sleep(2)
        self.goodCode(value)
        time.sleep(2)
        self.clickSearch
        time.sleep(2)
        self.assertequal(value, self.listGoods1)

if __name__ == '__main__':
    unittest.main(verbosity=2)