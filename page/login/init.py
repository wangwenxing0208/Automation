# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   init
  Description :
  Author :    star
  date：     2021/8/16
-------------------------------------------------
  Change Activity:
          2021/8/16:
-------------------------------------------------
"""
__author__ = 'star'

import unittest
from base.browserDriver import BrowserDriver

class Init(unittest.TestCase):
    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)

    def tearDown(self):
        driver = BrowserDriver(self)
        self.driver = driver.quit_browser()