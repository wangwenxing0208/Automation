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
        self.move_to_element(self.systemConfiguration_loc)  # 移动到元素
        self.click(self.role_loc)  # 点击元素

    @property
    def advancedSearch(self):
        self.switch_to_frame(self.iframe)   # 切换到iframe
        self.click(self.pullDown_loc)   # 点击下拉框

    def roleCode(self, usercode):
        self.send_keys(self.roleCode_loc, usercode)     # 输入角色编码
        self.click(self.roleCodeSearch_loc) # 点击搜索按钮

    @property
    def listRoleCode1(self):
        return self.get_text(self.listroleCode1_loc)  # 获取角色编码
