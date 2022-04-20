# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:32 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By

class CustomerPlan(BrowserDriver):
    planCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[13]/div/a')
    customerPlan_loc = (By.LINK_TEXT, '客户要货计划')
    iframe = 'PlanCustomer'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[3]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomerPlan1_loc = (By.XPATH, '//*[@id="grid_PlanCustomerList_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickCustomerPlan(self):
        self.move_to_element(self.planCenter_loc)
        self.click(self.customerPlan_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listCustomerPlan1(self):
        return self.get_text(self.listCustomerPlan1_loc)