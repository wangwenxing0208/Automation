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
        self.move_to_element(self.creditCenter_loc)
        self.click(self.creditRecalcula_loc)

    def controlStrategy(self, value):
        self.switch_to_frame(self.iframe)
        self.send_key(self.controlStrategy_loc, value)

    def customerName(self, value):
        self.click(self.open_loc)
        self.send_key(self.customerName_loc)

    def clickRecalcula(self):
        self.click(self.Recalcula_loc)
        self.click(self.Recalcula_loc)

    @property
    def listCreditRecalcula1(self):
        return self.get_text(self.listCreditRecalcula1_loc)