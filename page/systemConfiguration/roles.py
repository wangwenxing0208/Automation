# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 2:33 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Roles(BrowserDriver):
    systemConfiguration_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[1]/div/a')
    role_loc = (By.LINK_TEXT, '角色')
    iframe = 'rolemgr'
    pullDown_loc = (By.ID, 'condionSearch')
    roleCode_loc = (By.ID, 's-loginName')
    roleCodeSearch_loc = (By.XPATH, '//*[@id="condition-row"]/dl/dd/div[2]/button/i')
    listroleCode1_loc = (By.XPATH, '//*[@id="roleList"]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]')

    @property
    def clickRoles(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.systemConfiguration_loc)).perform()
        self.find_element(*self.role_loc).click()

    @property
    def advancedSearch(self):
        self.driver.switch_to.frame(self.iframe)
        self.find_element(*self.pullDown_loc).click()

    def roleCode(self, usercode):
        self.find_element(*self.roleCode_loc).send_keys(usercode)
        self.find_element(*self.roleCodeSearch_loc).click()

    @property
    def listRoleCode1(self):
        return self.find_element(*self.listroleCode1_loc).text
