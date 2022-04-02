# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 12:19 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class SaleOutOrder(BrowserDriver):
    stockCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[5]/div/a')
    saleOutOrder_loc = (By.LINK_TEXT, '销售出库')
    iframe = 'stock_sale_out_order'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[3]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listSaleOutOrder1_loc = (By.XPATH, '//*[@id="grid_complex_content_tbody"]/tr[1]/td[7]/div')

    @property
    def clickSaleOutOrder(self):
        self.move_to_element(self.stockCenter_loc)
        self.click(self.saleOutOrder_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listSaleOutOrder1(self):
        self.click(self.listSaleOutOrder1_loc)