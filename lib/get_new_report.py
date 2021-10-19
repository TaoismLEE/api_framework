# _*_ coding:utf-8 _*_
import os


def get_new_report(testreport):
    """
    获取最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new
