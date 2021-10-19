# _*_ coding:utf-8 _*_

import unittest
import requests
import ddt
from lib.read_excel import ReadExcel
from lib.send_requests import SendRequests
from lib.write_excel import WriteExcel
from lib.parse_file import generate_file_path
from lib.log import logger

case_file = generate_file_path("DemoAPITestCase_Flow.xlsx", flag='c')
report_file = generate_file_path("DemoAPITestCase_Flow.xlsx", flag='r')
testData = ReadExcel(case_file, "Sheet1").read_data()


@ddt.ddt
class Flow_Demo_API(unittest.TestCase):
    """XXX系统"""
    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    def call_api(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求头: {0}".format(data['headers']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re = SendRequests().sendRequests(self.s, data)
        # 获取服务端返回的值
        self.result = re.json()
        print("页面返回信息：%s" % re.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        try:
            int(self.result["code"])
        except KeyError:
            print("API does NOT have status property, we think of it success if len(response) > 0!")
            if len(self.result) > 0:
                OK_data = "PASS"
                print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                WriteExcel(report_file, case_file).write_data(rowNum + 1, OK_data, self.result)
        else:
            readData_code = int(data['status_code'])
            readData_msg = data["msg"]
            if readData_msg:
                if readData_code == self.result['code'] and readData_msg == self.result['msg']:
                    OK_data = "PASS"
                    print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                    WriteExcel(report_file,case_file).write_data(rowNum + 1, OK_data, self.result)
                if readData_code != self.result['code'] or readData_msg != self.result['msg']:
                    NOT_data = "FAIL"
                    print("用例测试结果:  {0}---->{1}", format(data['ID'], NOT_data))
                    WriteExcel(report_file, case_file).write_data(rowNum + 1, NOT_data, self.result)
                self.assertEqual(self.result['code'], readData_code, "返回实际结果是->:%s" % self.result['code'])
                self.assertEqual(self.result['msg'], readData_msg, "返回实际结果是->:%s" % self.result['msg'])
            else:
                if readData_code == self.result['code']:
                    OK_data = "PASS"
                    print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                    WriteExcel(report_file, case_file).write_data(rowNum + 1, OK_data, self.result)
                if readData_code != self.result['code']:
                    NOT_data = "FAIL"
                    print("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
                    WriteExcel(report_file, case_file).write_data(rowNum + 1, NOT_data, self.result)
                self.assertEqual(self.result['code'], readData_code, "返回实际结果是->:%s" % self.result['code'])

    @ddt.data(*testData)
    def test_flow_api(self, data):
        """
        数据驱动从第1个接口往下执行，因此通过if判断当前正在执行的接口
        执行后续依赖接口，可能会用到之前接口的返回数据如token或者从数据库拿数据，则可以在每个接口执行前重构data参数
        """
        if data['ID'] == 'login_trigger_001':
            self.call_api(data)
        if data['ID'] == 'project_load_002':
            """
            通过从之前接口返回结果或是数据库查询数据进行data参数重构
            """
            tempData = ReadExcel(report_file, "Sheet1").read_data()
            pre_api_response = [item for item in tempData if item['ID'] == 'login_trigger_001']
            authorization = "Bearer " + eval(pre_api_response[0]['response'])['access_token']
            headers = eval(data['headers'])
            headers['Authorization'] = authorization
            data['headers'] = str(headers)
            self.call_api(data)


if __name__ == '__main__':
    unittest.main()
