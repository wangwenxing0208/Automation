# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 3:19 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class PromotionActivity(BrowserDriver):
    promotionCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[7]/div/a')
    promotionActivity_loc = (By.LINK_TEXT, '促销活动')
    iframe = 'activity'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listPromotionActivity1_loc = (By.XPATH, '//*[@id="grid_complex_content_tbody"]/tr[1]/td[1]/div')

    @property
    def clickPromotionActivity(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.promotionCenter_loc)).perform()
        self.find_element(*self.promotionActivity_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(3)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listPromotionActivity1(self):
        return self.find_element(*self.listPromotionActivity1_loc).text