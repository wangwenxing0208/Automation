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
        ActionChains(self.driver).move_to_element(self.find_element(*self.settlementCenter_loc)).perform()
        self.find_element(*self.searchRemainMoney_loc).click()

    def financeOrganizationName(self, value1):
        self.driver.switch_to.frame(self.iframe)
        time.sleep(3)
        self.find_element(*self.financeOrganization_loc).send_keys(value1)

    def reconciliationDate(self):
        self.find_element(*self.reconciliationDate_loc).click()
        time.sleep(3)
        self.find_element(*self.date_loc).click()
        time.sleep(3)
        self.find_element(*self.date_loc).click()
        # js = "document.getElementByXpath(startDate_loc).removeAttribute('readonly')"
        # self.driver.execute_script(js)
        # js2 = "document.getElementByXpath(endDate_loc).removeAttribute('readonly')"
        # self.driver.execute_script(js2)
        # self.find_element(*self.startDate_loc).send_keys('002021/06/06')
        # self.find_element(*self.endDate_loc).send_keys('002021/06/06')


    def customerName(self, value2):
        self.find_element(*self.open_loc).click()
        time.sleep(3)
        self.find_element(*self.customerName_loc).send_keys(value2)

    def clickSearch(self):
        self.find_element(*self.search_loc).click()

    @property
    def listSearchRemainMoney1(self):
        return self.find_element(*self.listSearchRemainMoney1_loc).text