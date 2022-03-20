# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 8:33 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class CreditRecalcula(BrowserDriver):
    creditCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[8]/div/a')
    creditRecalcula_loc = (By.LINK_TEXT, '信用占用重算')
    iframe = 'creditrecalcula'
    controlStrategy_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    open_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[1]/a/i')
    customerName_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[7]/div/input')
    Recalcula_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCreditRecalcula1_loc = (By.XPATH, '//*[@id="grid_complex_content_tbody"]/tr/td[1]/div')

    @property
    def clickCreditRecalcula(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.creditCenter_loc)).perform()
        self.find_element(*self.creditRecalcula_loc).click()

    def controlStrategy(self, value):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(8)
        self.find_element(*self.controlStrategy_loc).send_keys(value)

    def customerName(self, value):
        self.find_element(*self.open_loc).click()
        time.sleep(2)
        self.find_element(*self.customerName_loc).send_keys(value)
        time.sleep(2)

    def clickRecalcula(self):
        self.find_element(*self.Recalcula_loc).click()
        self.find_element(*self.Recalcula_loc).click()

    @property
    def listCreditRecalcula1(self):
        return self.find_element(*self.listCreditRecalcula1_loc).text