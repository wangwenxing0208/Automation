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
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomer1_loc = (By.XPATH, '//*[@id="grid_buoyancyfactorlist_content_tbody"]/tr/td[1]/div/a')

    @property
    def clickCustomer(self):
        self.move_to_element(self.dhanneCenter_loc)
        self.click(self.customer_loc)

    def customerCode(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.customerCode_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)
        self.find_element(*self.search_loc).click()

    @property
    def listCustomer1(self):
        return self.get_text(self.listCustomer1_loc)