# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/6 8:37 下午
  Author     ：star
"""

from page.login.init import *
from page.systemConfiguration.roles import *
from common.login import *
import time

class TestcaseRoles(Init,Roles,Login):
    def test_roles(self, value='EC_JXS'):
        '''角色是否能够正常打开，查询是否正常'''
        self.successLogin()
        self.clickRoles
        time.sleep(3)
        self.advancedSearch
        time.sleep(3)
        self.roleCode(value)
        time.sleep(3)
        self.assertEqual(self.listRoleCode1, value)

if __name__ == '__main__':
    unittest.main(verbosity=2)