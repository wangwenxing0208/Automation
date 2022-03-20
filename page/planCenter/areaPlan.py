# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:40 下午
  Author     ：star
"""
""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class AreaPlan(BrowserDriver):
    planCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[11]/div/a')
    areaPlan_loc = (By.LINK_TEXT, '区域要货计划')
    iframe = 'PlanMarketArea'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listAreaPlan1_loc = (By.XPATH, '//*[@id="grid_PlanAreaList_content_tbody"]/tr[1]/td[2]/div')

    @property
    def clickAreaPlan(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.planCenter_loc)).perform()
        self.find_element(*self.areaPlan_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(10)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listAreaPlan1(self):
        return self.find_element(*self.listAreaPlan1_loc).text