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

from page.login.init import *
from page.systemConfiguration.users import *
from common.login import *
import time

class TestcaseUsers(Init,Users,Login):
    def test_users(self, value='232004'):
        '''用户是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickUser
        time.sleep(3)
        self.advancedSearch
        time.sleep(3)
        self.userCode(value)
        time.sleep(3)
        self.assertEqual(self.listUserCode1, value)



if __name__ == '__main__':
    unittest.main(verbosity=2)