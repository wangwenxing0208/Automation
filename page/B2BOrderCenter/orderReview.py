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
        self.move_to_element(self.B2BOrderCenter_loc)
        self.click(self.orderReview_loc)

    @property
    def state(self):
        self.switch_to_frame(self.iframe)
        self.click(self.open_loc)
        self.click(self.state_loc)
        self.click(self.stateALL_loc)
        self.switch_to_default_content()

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listOrderReview1(self):
        return self.get_text(self.listOrderReview1_loc)