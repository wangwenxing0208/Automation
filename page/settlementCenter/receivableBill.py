# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:26 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class ReceivableBill(BrowserDriver):
    settlementCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[6]/div/a')
    receivableBill_loc = (By.LINK_TEXT, '应收单')
    iframe = 'receivablebill'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listReceivableBill1_loc = (By.XPATH, '//*[@id="grid_head_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickReceivableBill(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.settlementCenter_loc)).perform()
        self.find_element(*self.receivableBill_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(3)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listReceivableBill1(self):
        return self.find_element(*self.listReceivableBill1_loc).text