# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 5:52 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class OrderReview(BrowserDriver):
    B2BOrderCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[4]/div/a')
    orderReview_loc = (By.LINK_TEXT, '订单财审')
    iframe = 'orderreview'
    open_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[1]/a')
    state_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[4]/div')
    stateALL_loc = (By.XPATH, '/html/body/ul/li[1]')
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listOrderReview1_loc = (By.XPATH, '//*[@id="grid_template_showuigrid_simpleList_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickOrderReview(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.B2BOrderCenter_loc)).perform()
        self.find_element(*self.orderReview_loc).click()

    @property
    def state(self):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.open_loc).click()
        time.sleep(2)
        self.find_element(*self.state_loc).click()
        time.sleep(2)
        self.find_element(*self.stateALL_loc).click()
        self.driver.switch_to.default_content()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.organization_loc).clear()
        time.sleep(2)
        self.find_element(*self.organization_loc).send_keys(value)
        time.sleep(2)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listOrderReview1(self):
        return self.find_element(*self.listOrderReview1_loc).text