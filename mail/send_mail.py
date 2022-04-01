# -*- coding: utf-8 -*-
"""
--------------------------------------------
  File Name:    send_mail
  Description:实现邮件报告的发送
  Author:   star
  Date:    2022/3/19
--------------------------------------------
  Change Activity:
           2022/3/19
--------------------------------------------
"""
__author__ = 'star'

import smtplib
from email.mime.text import MIMEText    #主要处理邮件正文信息
from email.mime.multipart import MIMEMultipart
from mail.read_ini import ReadIni
from data.config import Config
from utils.logger import Logger
import sys

logger = Logger(logger="mail").getlog()

#固定常量，mail配置文件的所在位置
mail_path = Config().path() + '\mail\mail.ini'
path = Config().path()

class SendMail(object):
    #在创建对象时就完成邮件用户信息的初始化
    def __init__(self):
        read = ReadIni()
        self.get_mail_config = read.read_ini(mail_path, "mail_config")
        self.get_cc = self.get_mail_config["cc"]
        self.get_bcc = self.get_mail_config["bcc"]

    #处理to_addr中传递给send_mail的参数
    def to_addr(self):
        try:
            get_to_addr = self.get_mail_config["to_addr"]
            get_list = get_to_addr.split(",")
            if len(self.get_cc) != 0:
                get_list += self.get_cc.split(",")
            if len(self.get_bcc) != 0:
                get_list += self.get_bcc.split(",")
            return get_list
        except:
            logger.error("收件人信息处理失败")

    #将发件人的信息进行处理
    def from_addr(self):
        try:
            get_from_addr = self.get_mail_config["from_addr"]
            return get_from_addr.split("@")[0]+"<%s>"%get_from_addr
        except:
            logger.error("发件人信息处理失败")

    def show_to_addr(self):
        return  ",".join([value.split("@")[0]+"<%s>"%value for value in self.get_mail_config["to_addr"].split(",")])

    #声明一个构建完整邮件的方法，通过MIMEMultipart完成附件和文本邮件的构成
    #邮件除了发送者、接受者，还有抄送者、密送者
    def create_mail(self, subject, message, reportname, reportpath):
        mail = MIMEMultipart()
        mail["Subject"] = subject
        mail["From"] = self.from_addr()
        #此处的To需要的是字符串信息而不是列表对象
        mail["To"] = self.show_to_addr()
        #添加从抄送者和密送者，后期可自动选择；此处ini中存在一个坑；会将在所有的文件中读取出来的键名全部默认为小写
        mail["Cc"] = self.get_cc
        mail["Bcc"] = self.get_bcc
        mail.attach(self.create_text(message))
        mail.attach(self.create_attach(reportname, reportpath))
        logger.info("邮件创建成功")
        return mail

    #创建邮件附件
    def create_attach(self, reportname, reportpath):
        #使用MIMEText完成一个文件的读取操作
        with open(reportpath, mode = "rb") as fp:
            # _subtype:表示指定文本类型的子类型；默认是文本类型；text/html、text/xml、
        # text/json、application/www--xxxx-from、application/octet-stream
        # 对应的content-type类型，类似处理12306火车订票系统中验证码的方式，将文件以
        # 二进制流的形式写入指定的位置
        attach = MIMEText(fp.read(), _subtype="base64", _charset="utf-8")
        #为了能够上传任意格式的文件，将文件的父类型定义为二进制流
        attach["Content-Type"] = "application/octet-stream"
        attach.add_header('Content-Disposition', 'attachment', filename = '%s'%reportname)
        return attach

    #封装一封邮件，在python中必须使用email模块
    #创建一个邮件文本
    def create_text(self, message):
        message_object = MIMEText(message, _charset="utf-8")
        return message_object

    #与邮件服务器建立会话连接
    def send_mail(self, subject, messgae, reportname, reportpath):
        try:
            #创建SMTP的会话连接对象
            get_smpt = smtplib.SMTP(host = self.get_mail_config["mail_server"])
            #实现登录操作：login中传入的是实现SMTP服务授权的用户名、密码，而不是前台登录的用户名、密码
            get_smpt.login(self.get_mail_config["mail_user"], self.get_mail_config["mail_password"])
            #登录成功后发送邮件：声明发送者、接收者、收件信息；发送的信息过于简单或者过于敏感，邮件服务器都会将其屏蔽
            #发送时出现554状态，可以考虑发送的信息及邮件的完整性
            #问题（声明邮件头的发送者、接收者等信息）
            get_smpt.sendmail(self.get_mail_config["from_addr"], self.to_addr(),
                              self.create_mail(subject, messgae, reportname,reportpath).as_string())
            logger.info("邮件发送成功")
        except:
            logger.error(sys.exc_info())