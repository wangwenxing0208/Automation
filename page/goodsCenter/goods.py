# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 8:57 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Goods(BrowserDriver):
    goodsCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[3]/div/a')
    goods_loc = (By.LINK_TEXT, '商品')
    iframe = 'baseGoods'
    goodCode_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listGoods1_loc = (By.XPATH, '//*[@id="grid_simple1_content_tbody"]/tr/td[1]/div/a')

    @property
    def clickGoods(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.goodsCenter_loc)).perform()
        self.find_element(*self.goods_loc).click()

    def goodCode(self, value):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.goodCode_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listGoods1(self):
        return self.find_element(*self.listGoods1_loc).text