# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:05 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CustomerFlowAccount(BrowserDriver):
    marketCastCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[9]/div/a')
    customerFlowAccount_loc = (By.LINK_TEXT, '客户费用流水账')
    iframe = 'cusflowacc'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    customerName_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[3]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomerFlowAccount1_loc = (By.XPATH, '//*[@id="grid_potype_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickCustomerFlowAccount(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.marketCastCenter_loc)).perform()
        self.find_element(*self.customerFlowAccount_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(10)
        self.find_element(*self.organization_loc).send_keys(value)
        time.sleep(2)

    def customerName(self, value):
        self.find_element(*self.customerName_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCustomerFlowAccount1(self):
        return self.find_element(*self.listCustomerFlowAccount1_loc).text