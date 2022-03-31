# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   qdy
  Description :
  Author :    star
  date：     2021/8/16
-------------------------------------------------
  Change Activity:
          2021/8/16:
-------------------------------------------------
"""
__author__ = 'star'

from base.seleniums import *
from selenium.webdriver.common.by import By

class Login(BrowserDriver):
    username_loc = (By.XPATH, '//*[@id="usernamebox"]/input')
    password_loc = (By.XPATH, '//*[@id="userpassword"]/input')
    login_loc = (By.ID, 'loginBtn')
    loginError_loc = (By.XPATH, '//*[@id="usernamebox"]/span[2]')

    def typeUserName(self, username):
        self.send_key(self.username_loc, username)

    def typePassword(self, password):
        self.send_key(self.password_loc, password)

    @property
    def clickLogin(self):
        self.click(self.login_loc)

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getLoginError(self):
        '''获取错误的信息'''
        return self.get_text(self.loginError_loc)
