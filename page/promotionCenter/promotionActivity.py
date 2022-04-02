# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 3:19 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By

class PromotionActivity(BrowserDriver):
    promotionCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[7]/div/a')
    promotionActivity_loc = (By.LINK_TEXT, '促销活动')
    iframe = 'activity'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listPromotionActivity1_loc = (By.XPATH, '//*[@id="grid_complex_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickPromotionActivity(self):
        self.move_to_element(self.promotionActivity_loc)
        self.click(self.promotionActivity_loc)

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listPromotionActivity1(self):
        return self.get_text(self.listPromotionActivity1_loc)