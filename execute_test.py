# _*_ coding:utf-8 _*_

import unittest
import time
from config import setting
from lib.send_email import SendMail
from lib.get_new_report import get_new_report
from db_init import init_data
from lib.HTMLTestRunner import HTMLTestRunner


def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover


def run_case(all_case, result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # # 初始化接口测试数据
    # init_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='XXX系统接口自动化测试报告', description='环境：xxxx 浏览器：xxxx', tester='XXX')
    runner.run(all_case)
    fp.close()
    # # 调用模块获取最新的报告
    # report = get_new_report(setting.TEST_REPORT)
    # # 调用发送邮件模块
    # obj_email = SendMail(report, "outlook")
    # obj_email.send_email()


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
