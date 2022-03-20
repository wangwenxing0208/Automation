# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:05 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class ChannelStock(BrowserDriver):
    stockCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[5]/div/a')
    ChannelStock_loc = (By.LINK_TEXT, '全渠道库存查询')
    iframe = 'channelOnhand'
    customer_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listChannelStock1_loc = (By.XPATH, '//*[@id="grid_simple1_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickChannelStock(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.stockCenter_loc)).perform()
        self.find_element(*self.ChannelStock_loc).click()

    def customerName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(3)
        self.find_element(*self.customer_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listChannelStock1(self):
        return self.find_element(*self.listChannelStock1_loc).text