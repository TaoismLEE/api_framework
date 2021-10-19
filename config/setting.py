# _*_ coding:utf-8 _*_

import os
import sys
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)

# 配置文件
TEST_CONFIG = os.path.join(PROJECT_PATH, "config", "db.ini")
# 测试用例程序文件
TEST_CASE = os.path.join(PROJECT_PATH, "testcase")
# 测试用例报告
TEST_REPORT = os.path.join(PROJECT_PATH, "report")


# outlook email config
MAIL_HOST = "shintsmtp.deloitte.com.cn"
MAIL_PORT = 25
MAIL_USER = ""
MAIL_PWD = ""
MAIL_SENDER = "yuliy@deloitte.com.cn"

# mail receivers
MAIL_RECEIVERS = ["yuliy@deloitte.com.cn"]
# MAIL_RECEIVERS = ["yuliy@deloitte.com.cn",
#                   "erizhu@deloitte.com.cn"]

# mail subject
MAIL_SUBJECT = "eDMS项目 - 接口自动化测试结果"

