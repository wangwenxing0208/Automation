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
        self.move_to_element(self.B2BOrderCenter_loc)
        self.click(self.returnOrder_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listReturnOrder1(self):
        return self.get_text(self.listReturnOrder1_loc)