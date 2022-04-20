# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   distributionContract
  Description :
  Author :    wangwenxing
  date：     2022/4/10
-------------------------------------------------
  Change Activity:
          2022/4/10:
-------------------------------------------------
"""
__author__ = 'wangwenxing'

from base.seleniums import *
from selenium.webdriver.common.by import By

class DistributionContract(BrowserDriver):
    econtractCenter_loc =  (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[11]/div/a')
    distributionContract_loc = (By.LINK_TEXT, '经销合同')
    iframe = 'contractTemplate'
    organization_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[1]/div')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listDistributionContract1_loc = (By.XPATH, '//*[@id="grid_buoyancyfactorlist_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickEcontractCenter(self):
        self.move_to_element(self.econtractCenter_loc)
        self.click(self.partyA_loc)

    def organization(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def search(self):
        self.click(self.search_loc)

    @property
    def listDistributionContract1(self):
        return self.get_text(self.listDistributionContract1_loc)