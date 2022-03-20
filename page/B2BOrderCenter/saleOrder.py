# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:18 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class SaleOrder(BrowserDriver):
    B2BOrderCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[4]/div/a')
    saleOrder_loc = (By.LINK_TEXT, '销售订单')
    iframe = 'saleorder'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listSaleOrder1_loc = (By.XPATH, '//*[@id="grid_template_showuigrid_salesorderList_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickSaleOrder(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.B2BOrderCenter_loc)).perform()
        self.find_element(*self.saleOrder_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.organization_loc).clear()
        time.sleep(3)
        self.find_element(*self.organization_loc).send_keys(value)
        time.sleep(3)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listSaleOrder1(self):
        return self.find_element(*self.listSaleOrder1_loc).text