# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   test
  Description :
  Author :    star
  date：     2021/9/15
-------------------------------------------------
  Change Activity:
          2021/9/15:
-------------------------------------------------
"""
__author__ = 'star'

import logging

from utils.logger import Logger

class aaa(Logger):
    def bbb(self):
        logging.info('12331')


if __name__=='__main__':
    aaa().bbb(aaa='111')