# _*_ coding:utf-8 _*_


class SendRequests():
    """发送请求数据"""
    def sendRequests(self, s, apiData):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]

            if apiData["params"] == "":
                params = None
            else:
                params = eval(apiData["params"])

            if apiData["headers"] == "":
                headers = None
            else:
                headers = eval(apiData["headers"])

            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])

            type = apiData["type"]
            if type == "data":
                body = body_data
            else:
                body = params

            # 发送请求
            re = s.request(method=method, url=url, headers=headers, data=body)
            return re
        except Exception as e:
            print(e)
