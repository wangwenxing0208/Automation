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
        self.move_to_element(self.marketCastCenter_loc)
        self.click(self.customerCast_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listCustomerCast1(self):
        return self.get_text(self.listCustomerCast1_loc)