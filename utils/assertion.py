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

logger = Logger(logger='Assert').getlog()   # 实例化logger

class Assertion(object):     # 创建一个类，类名为Assertion

    def assertequal(self, expect, actual):  # 断言相等
        try:
            self.assertEqual(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertnotequal(self, expect, actual):   # 断言不相等
        try:
            self.assertNotEqual(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertin(self, expect, actual): # 断言在列表中
        try:
            self.assertIn(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertnotin(self, expect, actual):  # 断言不在列表中
        try:
            self.assertNotIn(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def asserttrue(self, expect, actual):   # 断言为True
        try:
            self.assertTrue(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertfalse(self, expect, actual):
        try:
            self.assertFalse(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertis(self, expect, actual):
        try:
            self.assertIs(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise

    def assertisnot(self, expect, actual):
        try:
            self.assertIsNot(expect, actual)
            logger.info('预期结果：%s，测试结果：%s，测试通过' % (expect, actual))
        except Exception as e:
            logger.error('预期结果：%s，测试结果：%s，测试不通过' % (expect, actual))
            logger.error('错误信息：%s' % e)
            raise