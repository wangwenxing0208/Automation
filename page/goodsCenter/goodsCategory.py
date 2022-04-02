# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/8 4:09 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GoodsCategory(BrowserDriver):
    goodsCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[3]/div/a')
    goodsCategory_loc = (By.LINK_TEXT, '商品分类')
    iframe = 'goodscategory'
    goodCategoryode_loc = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/ui-searchbox/div/div[3]/div[2]/a[2]')
    listGoodsCategory1_loc = (By.XPATH, '//*[@id="grid_simple1_content_tbody"]/tr[1]/td[1]/div/a')

    @property
    def clickGoodsCategory(self):
        self.move_to_element(*self.goodsCenter_loc)
        self.click(*self.goodsCategory_loc)

    def goodCategoryCode(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.goodCategoryode_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listGoodsCategory1(self):
        return self.get_text(self.listGoodsCategory1_loc)