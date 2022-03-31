# -*- coding: utf-8 -*-
"""
--------------------------------------------
  File Name:    browserDriver
  Description:
  Author:   star
  Date:    2022/3/17
--------------------------------------------
  Change Activity:
           2022/3/17
--------------------------------------------
"""
__author__ = 'star'


import platform
from selenium import webdriver
from utils.logger import Logger
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from data.config import Config


logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    # path = './drivers/'#这是获取相对路径的方法

    c = Config()
    path = c.path() + '/drivers/'

    if platform.system() == 'Windows':  #windows系统
        logger.info('获取到操作系统类型：Windows')
        chrome_driver_path = path + 'chromedriver.exe'
        logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)
        ie_driver_path = path + 'IEDriverServer.exe'
    elif platform.system() == 'Linux':  #linux系统
        logger.info('获取到操作系统类型：Linux')
        chrome_driver_path = path + 'chromedriver_linux'
        logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)
    elif platform.system() == 'Darwin':  #mac系统
        logger.info('获取到操作系统类型：Mac')
        chrome_driver_path = path + 'chromedriver'
        logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)
    else:
        logger.info('未获取到操作系统类型')

    def __init__(self, driver):
        self.driver = driver
        self.c = Config()

    def openbrowser(self, driver):
        browser = self.c.get("browserType", "browserName")
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = self.c.get('pathUrl', "URL")
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            s = Service(self.chrome_driver_path)
            # driver = webdriver.Chrome(service=s, options=chrome_options)
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=chrome_options) #用于Windows系统加载驱动使用
            # driver = webdriver.Chrome() #用于linux系统加载驱动使用
            logger.info("启动谷歌浏览器")
        else:
            logger.error("启动浏览器失败")

        driver.get(url)
        logger.info("打开URL: %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()