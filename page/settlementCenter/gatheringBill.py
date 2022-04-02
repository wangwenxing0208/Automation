# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:33 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By

class GatheringBill(BrowserDriver):
    settlementCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[6]/div/a')
    gatheringBill_loc = (By.LINK_TEXT, '收款单')
    iframe = 'gatheringbill'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listGatheringBill1_loc = (By.XPATH, '//*[@id="grid_salesorder_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickGatheringBill(self):
        self.move_to_element(self.settlementCenter_loc)
        self.click(self.gatheringBill_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listGatheringBill1(self):
        return self.get_text(self.listGatheringBill1_loc)