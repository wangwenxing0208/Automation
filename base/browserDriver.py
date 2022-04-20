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
import sys

logger = Logger(logger="BrowserDriver").getlog()    # 日志

class BrowserDriver(object):    # 创建浏览器驱动类
    c = Config()    # 创建配置文件对象
    path = c.path() + '/drivers/'    # 定义驱动路径

    def __init__(self, driver):   # 初始化浏览器驱动
        self.driver = driver    # 初始化浏览器驱动
        self.c = Config()    # 初始化配置文件对象

    def openbrowser(self, driver):  # 打开浏览器
        browser = self.c.get("browserType", "browserName")  # 获取浏览器类型
        logger.info("选择的浏览器为: %s 浏览器" % browser)    # 打印浏览器类型
        url = self.c.get('pathUrl', "URL")  # 获取测试网址
        logger.info("测试的URL为: %s" % url)    # 打印测试网址
        if browser == "Firefox":    # 判断浏览器类型
            driver = webdriver.Firefox()    # 创建Firefox浏览器对象
            logger.info("启动火狐浏览器")  # 打印启动火狐浏览器
        elif browser == "Chrome":    # 判断浏览器类型
            chrome_options = webdriver.ChromeOptions()  # 创建Chrome浏览器对象
            chrome_options.add_argument('--no-sandbox')     # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')    # 窗口最大化
            chrome_options.add_argument('--disable-gpu')    # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')    # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')   # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')    # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')   # 禁用扩展
            chrome_options.add_argument('lang=zh_CN.UTF-8')   # 设置默认编码
            if platform.system() == 'Windows':  # windows系统
                logger.info('获取到操作系统类型：Windows')    # 打印操作系统类型
                chrome_driver_path = self.path + 'chromedriver.exe' # 获取chromedriver路径
                logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)    # 打印浏览器驱动路径
                ie_driver_path = self.path + 'IEDriverServer.exe'    # 获取IEDriverServer路径
                driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)    # 启动chrome浏览器
            elif platform.system() == 'Linux':  # linux系统
                logger.info('获取到操作系统类型：Linux')  # 打印操作系统类型
                chrome_driver_path = self.path + 'chromedriver_linux'    # 获取chromedriver路径
                logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)
                driver = webdriver.Chrome()
            elif platform.system() == 'Darwin':  # mac系统
                logger.info('获取到操作系统类型：Mac')
                chrome_driver_path = self.path + 'chromedriver'
                logger.info('获取浏览器驱动路径：%s' % chrome_driver_path)
                s = Service(chrome_driver_path)
                driver = webdriver.Chrome(service=s, options=chrome_options)
            else:
                logger.info('未获取到操作系统类型')

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