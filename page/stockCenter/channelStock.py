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
        self.move_to_element(self.stockCenter_loc)
        self.click(self.ChannelStock_loc)

    def customerName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.customer_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listChannelStock1(self):
        return self.get_text(self.listChannelStock1_loc)