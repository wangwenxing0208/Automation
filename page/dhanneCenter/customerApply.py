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
        ActionChains(self.driver).move_to_element(self.find_element(*self.dhanneCenter_loc)).perform()
        self.find_element(*self.customerApply_loc).click()

    @property
    def state(self):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.open_loc).click()
        time.sleep(3)
        self.find_element(*self.state_loc).click()
        time.sleep(3)
        self.find_element(*self.stateALL_loc).click()
        self.driver.switch_to.default_content()

    def customerName(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.customerName_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCustomerApply1(self):
        return self.find_element(*self.listCustomerApply1_loc).text
