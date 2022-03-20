# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 8:54 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CustomerCast(BrowserDriver):
    marketCastCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[9]/div/a')
    customerCast_loc = (By.LINK_TEXT, '客户费用单')
    iframe = 'customercast'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomerCast1_loc = (By.XPATH, '//*[@id="grid_complex_content_tbody"]/tr[1]/td[2]/div')

    @property
    def clickCustomerCast(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.marketCastCenter_loc)).perform()
        self.find_element(*self.customerCast_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(10)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCustomerCast1(self):
        return self.find_element(*self.listCustomerCast1_loc).text