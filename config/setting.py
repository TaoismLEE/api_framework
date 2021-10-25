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
MAIL_HOST = ""
MAIL_PORT = 25
MAIL_USER = ""
MAIL_PWD = ""
MAIL_SENDER = ""

# mail receivers
MAIL_RECEIVERS = ["xxxx@xxxx"]
# MAIL_RECEIVERS = ["xxxx@xxxx",
#                   "xxxx@dxxxx"]

# mail subject
MAIL_SUBJECT = "xxxx项目 - 接口自动化测试结果"

