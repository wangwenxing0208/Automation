# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 4:20 下午
  Author     ：star
"""

from page.login.init import *
from page.systemConfiguration.ncSyncMonitor import *
from common.login import *
import time

class TestcaseNCSyncMonitor(Init,NCSyncMonitor,Login):
    def test_ncSyncMonitor(self, value='1'):
        '''NC同步监控是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickNCSyncMonitor
        time.sleep(3)
        self.clickSearch
        time.sleep(3)
        self.assertEqual(self.listNumber1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)