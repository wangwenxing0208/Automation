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
import time

class TestcaseLogin(Init,Login,HomePage):
    def test_Login(self):
        '''验证登陆成功'''
        self.login('wwx', '123qwe')
        time.sleep(3)
        self.assertEqual('王文星', self.UserName())

if __name__ == '__main__':
    unittest.main(verbosity=2)