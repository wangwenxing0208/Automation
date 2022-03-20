# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 2:37 下午
  Author     ：star
"""

from page.login.login import *

class Login(Login):
    def successLogin(self):
        '''成功登录'''
        self.login('wwx', '123qwe')

