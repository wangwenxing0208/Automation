# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   assert
  Description :
  Author :    wangwenxing
  date：     2022/4/1
-------------------------------------------------
  Change Activity:
          2022/4/1:
-------------------------------------------------
"""
__author__ = 'wangwenxing'

from utils.logger import Logger

logger = Logger(logger='Assert').getlog()

class Assertion(object):

    def assertequal(self, expect, actual):
        try:
            self.assertEqual(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise


