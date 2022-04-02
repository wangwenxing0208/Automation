# -*- coding: utf-8 -*-
"""
  Time       ：2021/9/7 4:22 下午
  Author     ：star
"""

from base.seleniums import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class NCSyncMonitor(BrowserDriver):
    systemConfiguration_loc = (By.XPATH, '//*[@id="portal"]/div[1]/div[1]/ul/li[1]/div/a')
    ncSyncMonitor_loc = (By.LINK_TEXT, 'NC同步监控')
    iframe = 'nc-sync-monitor'
    search_loc = (By.XPATH, '//*[@id="content"]/div[1]/ui-searchbox/div/div[3]/div[2]/a[2]')
    listNumber1_loc = (By.XPATH, '//*[@id="grid_simple_content_numCol"]/div[1]')

    @property
    def clickNCSyncMonitor(self):
        self.move_to_element(self.systemConfiguration_loc)     # 移动到系统配置
        self.click(self.ncSyncMonitor_loc)  # 点击NC同步监控

    @property
    def clickSearch(self):
        self.switch_to_frame(self.iframe)     # 切换到iframe
        self.click(self.search_loc)  # 点击搜索

    @property
    def listNumber1(self):
        return self.get_text(self.listNumber1_loc)  # 获取列表数量