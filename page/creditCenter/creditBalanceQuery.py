# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 8:18 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CreditBalanceQuery(BrowserDriver):
    creditCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[8]/div/a')
    creditBalanceQuery_loc = (By.LINK_TEXT, '信用余额查询')
    iframe = 'creditoccupy'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCreditBalanceQuery1_loc = (By.XPATH, '//*[@id="grid_creditlimit_content_tbody"]/tr[1]/td[2]/div')

    @property
    def clickCreditBalanceQuery(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.creditCenter_loc)).perform()
        self.find_element(*self.creditBalanceQuery_loc).click()

    def organizationName(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(6)
        self.find_element(*self.organization_loc).send_keys(value)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listCreditBalanceQuery1(self):
        return self.find_element(*self.listCreditBalanceQuery1_loc).text