# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/6 8:37 下午
  Author     ：star
"""

from page.login.init import *
from page.systemConfiguration.roles import *
from common.login import *
from utils.assertion import Assertion
import time

class TestcaseRoles(Init,Roles,Login,Assert):
    def test_roles(self, value='EC_JXS'):
        '''角色是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickRoles
        time.sleep(3)
        self.advancedSearch
        time.sleep(3)
        self.roleCode(value)
        time.sleep(3)
        self.assertequal(value, self.listRoleCode1)

if __name__ == '__main__':
    unittest.main(verbosity=2)