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
        ActionChains(self.driver).move_to_element(self.find_element(*self.goodsCenter_loc)).perform()
        self.find_element(*self.goodsCategory_loc).click()

    def goodCategoryCode(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.goodCategoryode_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listGoodsCategory1(self):
        return self.find_element(*self.listGoodsCategory1_loc).text