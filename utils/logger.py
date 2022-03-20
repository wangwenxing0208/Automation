# -*- coding: utf-8 -*-
"""
--------------------------------------------
  File Name:    logger
  Description:
  Author:   star
  Date:    2022/3/16
--------------------------------------------
  Change Activity:
           2022/3/16
--------------------------------------------
"""
__author__ = 'star'


import logging
import os.path
import time
from data.config import Config

class Logger(object):
    def __init__(self,logger):
        '''
        将日志保存到指定的路径文件中
        指定日志的级别，以及调用文件
        '''

        #创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handle，用来写入日志文件
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # log_path = './log/'
        path = Config().path()
        LOG_PATH = path + '/log/'
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)  # 如果不存在这个logs文件夹，就自动创建一个
        log_name = LOG_PATH+now+'.log'

        filehandle = logging.FileHandler(log_name, encoding="utf-8")
        filehandle.setLevel(logging.INFO)

        #创建一个handle，用来输入日志到控制台
        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        #将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        controlhandle.setFormatter(formatter)

        #给logger添加handle
        self.logger.addHandler(filehandle)
        self.logger.addHandler(controlhandle)

    def getlog(self):
        return self.logger

class GetLog(object):
    def __init__(self):
        self.get_log = logging.getLogger("test")
        self.get_log.setLevel(logging.INFO)

    #声明一个定义格式的方法
    def get_formatter(self):
        #定义日志格式
        get_formatter = logging.Formatter("%(asctime)s - %(filename)s\
                                          [level: %(levelname)s] - [lineNo: %(lineno)d]' %(pathname)s %(message)s")
        return get_formatter

    def get_handle(self, logpath):
        _get_handle = logging.FileHandler(logpath)
        _get_handle.setFormatter(self.get_formatter())
        self.logger.addHandler(_get_handle)
