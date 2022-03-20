# -*- coding: utf-8 -*-
"""
--------------------------------------------
  File Name:    run
  Description:
  Author:   star
  Date:    2022/3/17
--------------------------------------------
  Change Activity:
           2022/3/17
--------------------------------------------
"""
__author__ = 'star'


import os
import sys
import time
import unittest
import sys
sys.path.append('../')
from report.HTMLTestRunner3 import HTMLTestRunner

def create_suite():
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = './testCase'
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test_login.py',
        top_level_dir=None
    )

    for test_case in discover:
        TestSuite.addTests(test_case)
        # print(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'
        print(report_name)
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = './report/result.html'
        print(report_name)
    return report_name

def run():
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='渠道云巡检自动化测试报告',
        description='自动化测试用例执行情况'
    )
    Runner.run(TestSuite)
    fp.close()

if __name__ == '__main__':
    run()