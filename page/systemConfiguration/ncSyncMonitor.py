# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 4:22 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class NCSyncMonitor(BrowserDriver):
    systemConfiguration_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[1]/div/a')
    ncSyncMonitor_loc = (By.LINK_TEXT, 'NC同步监控')
    iframe = 'nc-sync-monitor'
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listNumber1_loc = (By.XPATH, '//*[@id="grid_simple_content_numCol"]/div[1]')

    @property
    def clickNCSyncMonitor(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.systemConfiguration_loc)).perform()
        self.find_element(*self.ncSyncMonitor_loc).click()

    @property
    def clickSearch(self):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.search_loc).click()

    @property
    def listNumber1(self):
        return self.find_element(*self.listNumber1_loc).text