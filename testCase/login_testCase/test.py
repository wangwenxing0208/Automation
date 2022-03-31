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

import platform

# 查看系统类型
print(platform.system())

if platform.system() == 'Windows':
    print('windows')
elif platform.system() == 'linux':
    print('linux')
elif platform.system() == 'Darwin':
    print('mac')
else:
    print('other')