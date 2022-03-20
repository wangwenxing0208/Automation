# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 4:44 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Customer(BrowserDriver):
    dhanneCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[2]/div/a')
    customer_loc = (By.LINK_TEXT, '客户档案')
    iframe = 'customer'
    customerCode_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    CustomerApply = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomer1_loc = (By.XPATH, '//*[@id="grid_buoyancyfactorlist_content_tbody"]/tr/td[1]/div/a')

    @property
    def clickCustomer(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.dhanneCenter_loc)).perform()
        self.find_element(*self.customer_loc).click()

    def customerCode(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.customerCode_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCustomer1(self):
        return self.find_element(*self.listCustomer1_loc).text