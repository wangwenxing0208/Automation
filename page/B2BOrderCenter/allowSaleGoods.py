# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 4:16 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By

class AllowSaleGoods(BrowserDriver):
    B2BOrderCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[4]/div/a')
    allowSaleGoods_loc = (By.LINK_TEXT, '允销目录')
    iframe = 'allowsaleproduct'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listAllowSaleGoods1_loc = (By.XPATH, '//*[@id="grid_AllowSaleProduct_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickAllowSaleGoods(self):
        self.move_to_element(self.B2BOrderCenter_loc)
        self.click(self.allowSaleGoods_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listAllowSaleGoods1(self):
        return self.get_text(self.listAllowSaleGoods1_loc)