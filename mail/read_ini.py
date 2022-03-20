# -*- coding: utf-8 -*-
"""
--------------------------------------------
  File Name:    read_ini
  Description:读取ini文件中的数据
  Author:   star
  Date:    2022/3/19
--------------------------------------------
  Change Activity:
           2022/3/19
--------------------------------------------
"""
__author__ = 'star'

import configparser
from data.config import Config

class ReadIni(object):

    def read_ini(self, ini_path, section_name):
        #声明一个dict，用于储存所有的数据，然后以关键字的形式传入
        dict1 = {}
        conf_read = configparser.ConfigParser()
        get_result = conf_read.read(ini_path, encoding="utf-8")
        for key, value in conf_read[section_name].items():
            dict1[key] = value
        return dict1

if __name__ == '__main__':
    mail_path = Config().path() + "\mail\mail.ini"
    read = ReadIni()
    print(mail_path)
    print(read.read_ini(mail_path, "mail_config"))