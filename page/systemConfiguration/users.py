# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/6 9:06 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Users(BrowserDriver):
    systemConfiguration_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[1]/div/a')
    user_loc = (By.LINK_TEXT, '用户')
    iframe = 'usermgr'
    pullDown_loc = (By.ID, 'condionSearch')
    userCode_loc = (By.ID, 's-loginName')
    userCodeSearch_loc = (By.XPATH, '//*[@id="condition-row"]/dl/dd/div[1]/button/i')
    listUserCode1_loc = (By.XPATH, '//*[@id="userList"]/div[1]/div[3]/div/table/tbody/tr/td[2]')

    @property
    def clickUser(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.systemConfiguration_loc)).perform()
        self.find_element(*self.user_loc).click()

    @property
    def advancedSearch(self):
        self.driver.switch_to.frame(self.iframe)
        self.click(self.pullDown_loc)

    def userCode(self, usercode):
        self.send_key(self.userCode_loc, usercode)
        self.click(self.userCodeSearch_loc)

    @property
    def listUserCode1(self):
        return self.get_text(self.listUserCode1_loc)






