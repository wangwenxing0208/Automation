# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   user_information
  Description :
  Author :    star
  date：     2021/8/31
-------------------------------------------------
  Change Activity:
          2021/8/31:
-------------------------------------------------
"""
__author__ = 'star'

from base.seleniums import *
from selenium.webdriver.common.by import By

class HomePage(BrowserDriver):
    username_im = (By.XPATH, '//*[@id="username"]/span[2]')

    def UserName(self):
        return self.find_element(*self.username_im).text

