# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 5:56 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CustomerApply(BrowserDriver):
    dhanneCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[2]/div/a')
    customerApply_loc = (By.LINK_TEXT, '客户申请单')
    iframe = 'cusReqForm'
    open_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[1]/a')
    state_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[12]/div')
    stateALL_loc = (By.XPATH, '/html/body/ul/li[1]')
    customerName_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomerApply1_loc = (By.XPATH, '//*[@id="grid_buoyancyfactorlist_content_tbody"]/tr/td[2]/div')

    @property
    def clickCustomerApply(self):
        self.move_to_element(self.dhanneCenter_loc)
        self.click(self.customerApply_loc)

    @property
    def state(self):
        self.switch_to_frame(self.iframe)
        self.click(self.open_loc)
        self.click(self.state_loc)
        self.click(self.stateALL_loc)
        self.switch_to_default_content()

    def customerName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.customerName_loc)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listCustomerApply1(self):
        return self.get_text(self.listCustomerApply1_loc)
