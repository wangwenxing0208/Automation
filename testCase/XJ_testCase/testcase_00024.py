# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:26 下午
  Author     ：star
"""

from page.login.init import *
from page.uniqueCode.traceFlow import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseTraceFlow(Init,TraceFlow,Login,Assertion):
    def test_traceFlow(self, value1='200326282629201890', value2='1'):
        '''追溯流行明细是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickTraceFlow
        time.sleep(2)
        self.boxCode(value1)
        time.sleep(2)
        self.clickSearch
        time.sleep(20)
        self.assertequal(value2, self.listTraceFlow1)


if __name__ == '__main__':
    unittest.main(verbosity=2)