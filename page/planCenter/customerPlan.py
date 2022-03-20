# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:32 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CustomerPlan(BrowserDriver):
    planCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[11]/div/a')
    customerPlan_loc = (By.LINK_TEXT, '客户要货计划')
    iframe = 'PlanCustomer'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[3]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCustomerPlan1_loc = (By.XPATH, '//*[@id="grid_PlanCustomerList_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickCustomerPlan(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.planCenter_loc)).perform()
        self.find_element(*self.customerPlan_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(10)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCustomerPlan1(self):
        return self.find_element(*self.listCustomerPlan1_loc).text