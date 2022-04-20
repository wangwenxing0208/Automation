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
sys.path.append('../')  # 将项目根目录加入到系统搜索路径中
from report.HTMLTestRunner3 import HTMLTestRunner   # 导入HTMLTestRunner

def create_suite(): # 创建测试套件
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = './testCase/XJ_testCase'   # 测试用例的目录
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover( # 找到测试用例
        start_dir=test_dir, # 测试用例的目录
        pattern='testcase_00001.py', # 测试用例文件名的匹配规则
        top_level_dir=None  # 测试用例的顶层目录
    )

    for test_case in discover:  # 循环加载测试用例
        TestSuite.addTests(test_case)   # 加载测试用例
        # print(test_case)  # 打印测试用例
    return TestSuite    # 返回测试套件

def report():   # 测试报告的路径
    if len(sys.argv) > 1:   # 判断是否有参数
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'    # 参数1为报告名称
        print(report_name)  # 打印报告名称
    else:   # 没有参数
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")   # 获取当前时间
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'    # 报告名称
        report_name = './report/result.html'    # 报告的名称
        print(report_name)  # 打印报告名称
    return report_name  # 返回报告名称

def run():  # 执行测试用例
    TestSuite = create_suite()  # 创建测试套件
    fp = open(report(), 'wb')   # 打开报告文件
    Runner = HTMLTestRunner(    # 实例化HTMLTestRunner
        stream=fp,   # 报告文件
        title='渠道云巡检自动化测试报告',   # 报告标题
        description='自动化测试用例执行情况'   # 报告描述
    )
    Runner.run(TestSuite)   # 执行测试套件
    fp.close()   # 关闭报告文件

if __name__ == '__main__':  # 判断是否为主程序运行
    run()   # 执行测试用例