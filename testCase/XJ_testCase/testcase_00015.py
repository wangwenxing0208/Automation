# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:19 上午
  Author     ：star
"""

from page.login.init import *
from page.stockCenter.channelStock import *
from common.login import *
import time

class TestcaseChannelStock(Init,ChannelStock,Login):
    def test_channelStock(self, value='哈尔滨迪亲商贸有限公司'):
        '''全渠道库存查询是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickChannelStock
        time.sleep(2)
        self.customerName(value)
        time.sleep(2)
        self.clickSearch
        self.assertEqual(self.listChannelStock1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)