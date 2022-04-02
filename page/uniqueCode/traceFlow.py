# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:19 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class TraceFlow(BrowserDriver):
    uniqueCode_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[10]/div/a')
    traceFlow_loc = (By.LINK_TEXT, '追溯流向明细')
    iframe = 'traceabilityinfo'
    boxCode_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listTraceFlow1_loc = (By.XPATH, '//*[@id="grid_warehouse_content_numCol"]/div[1]')

    @property
    def clickTraceFlow(self):
        self.move_to_element(self.uniqueCode_loc)
        self.click(*self.traceFlow_loc)

    def boxCode(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.boxCode_loc, value)

    @property
    def clickSearch(self):
        self.click(*self.search_loc)

    @property
    def listTraceFlow1(self):
        return self.get_text(self.listTraceFlow1_loc)