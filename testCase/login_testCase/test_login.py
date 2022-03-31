# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   test_qdy
  Description :
  Author :    star
  date：     2021/8/16
-------------------------------------------------
  Change Activity:
          2021/8/16:
-------------------------------------------------
"""
__author__ = 'star'

from page.login.init import *
from common.login import *
import unittest

class QdyTest(Init,Login):
    def test_qdyLoin(self, parent='divText', value='userNameNull'):
        '''登录业务：账号密码为空验证'''
        self.login('', '')
        self.assertEqual(self.getLoginError, '请输入正确用户名')

if __name__ == '__main__':
    unittest.main(verbosity=2)