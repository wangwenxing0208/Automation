# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/9 1:40 上午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

class SearchRemainMoney(BrowserDriver):
    settlementCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[6]/div/a')
    searchRemainMoney_loc = (By.LINK_TEXT, '应收余额查询')
    iframe = 'searchremainmoney'
    financeOrganization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[1]/div/input')
    reconciliationDate_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[1]/div[3]/div/span/span/input[1]')
    startDate_loc = (By.XPATH, '/html/body/div[16]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div')
    endDate_loc = (By.XPATH, '/html/body/div[16]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div')
    date_loc = (By.XPATH, '/html/body/div[16]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[4]')
    open_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[1]/a')
    customerName_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[4]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listSearchRemainMoney1_loc = (By.XPATH, '//*[@id="grid_head_content_tbody"]/tr[1]/td[3]/div')

    @property
    def clickSearchRemainMoney(self):
        self.move_to_element(self.settlementCenter_loc)
        self.click(self.searchRemainMoney_loc)

    def financeOrganizationName(self, value1):
        self.switch_to_frame(self.iframe)
        self.send_key(self.financeOrganization_loc, value1)

    def reconciliationDate(self):
        self.click(self.reconciliationDate_loc)
        self.click(self.date_loc)
        self.click(self.date_loc)


    def customerName(self, value2):
        self.click(self.open_loc)
        self.send_key(self.customerName_loc, value2)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listSearchRemainMoney1(self):
        return self.get_text(self.listSearchRemainMoney1_loc)