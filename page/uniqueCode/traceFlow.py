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
        ActionChains(self.driver).move_to_element(self.find_element(*self.uniqueCode_loc)).perform()
        self.find_element(*self.traceFlow_loc).click()

    def boxCode(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(2)
        self.find_element(*self.boxCode_loc).send_keys(value)

    @property
    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listTraceFlow1(self):
        return self.find_element(*self.listTraceFlow1_loc).text