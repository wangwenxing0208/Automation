# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   jdbcConnect
  Description :
  Author :    wangwenxing
  date：     2022/4/3
-------------------------------------------------
  Change Activity:
          2022/4/3:
-------------------------------------------------
"""
__author__ = 'wangwenxing'

#连接oracle数据库
import cx_Oracle
import os
import sys
class jdbcConnect:
    def __init__(self, host, port, user, password, serviceName):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.serviceName = serviceName
        self.conn = self.getConn()

    def getConn(self):
        try:
            conn = cx_Oracle.connect(self.user, self.password, self.host+':'+self.port+'/'+self.serviceName)
            return conn
        except Exception as e:
            print(e)
            sys.exit()

    def closeConn(self):
        self.conn.close()

    def getCursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()
