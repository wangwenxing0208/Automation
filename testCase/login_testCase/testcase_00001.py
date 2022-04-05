# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   test_login
  Description :
  Author :    star
  date：     2021/8/31
-------------------------------------------------
  Change Activity:
          2021/8/31:
-------------------------------------------------
"""
__author__ = 'star'

import unittest
from page.login.login import Login
from page.login.init import Init
from page.login.userHome import HomePage
from utils.logger import Logger
import time

logger = Logger(logger='TestCase').getlog()

class TestcaseLogin(Init,Login,HomePage):
    def test_Login(self):
        '''验证登陆成功'''
        self.login('wwx', '123qwe')
        time.sleep(3)
        try:
            self.assertEqual('王文星1', self.UserName())
            logger.info('预期结果：王文星1，测试结果：%s，测试通过' % self.UserName())
        except:
            logger.error('预期结果：王文星1，测试结果：%s，测试不通过' % self.UserName())
            raise

if __name__ == '__main__':
    unittest.main(verbosity=2)