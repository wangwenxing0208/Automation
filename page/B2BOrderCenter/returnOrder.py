# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 11:45 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ReturnOrder(BrowserDriver):
    B2BOrderCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[4]/div/a')
    returnOrder_loc = (By.LINK_TEXT, '退货订单')
    iframe = 'rejectorder'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listReturnOrder1_loc = (By.XPATH, '//*[@id="grid_template_showuigrid_salesorderList_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickReturnOrder(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.B2BOrderCenter_loc)).perform()
        self.find_element(*self.returnOrder_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listReturnOrder1(self):
        return self.find_element(*self.listReturnOrder1_loc).text