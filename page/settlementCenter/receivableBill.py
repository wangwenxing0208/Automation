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
        self.move_to_element(self.settlementCenter_loc)
        self.click(self.receivableBill_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listReceivableBill1(self):
        return self.get_text(self.listReceivableBill1_loc)