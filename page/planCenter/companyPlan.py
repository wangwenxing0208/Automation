# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/13 9:40 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time




class CompanyPlan(BrowserDriver):
    planCenter_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[11]/div/a')
    companyPlan_loc = (By.LINK_TEXT, '公司要货计划')
    iframe = 'PlanCompany'
    organization_loc = (By.XPATH, '/html/body/div[2]/div[1]/div/div/div[1]/ui-searchbox/div/div[1]/div[2]/div/input')
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listCompanyPlan1_loc = (By.XPATH, '//*[@id="grid_PlanCompanyList_content_tbody"]/tr[1]/td[2]/div')

    @property
    def clickCompanyPlan(self):
        self.move_to_element(self.planCenter_loc)
        self.click(self.companyPlan_loc)    # 点击公司要货计划

    def organizationName(self, value):
        self.switch_to_frame(self.iframe)    # 切换到iframe
        self.send_key(self.organization_loc, value)

    def clickSearch(self):
        self.click(self.search_loc)

    @property
    def listCompanyPlan1(self):
        return self.get_text(self.listCompanyPlan1_loc)


