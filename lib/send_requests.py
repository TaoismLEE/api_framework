# _*_ coding:utf-8 _*_


class SendRequests():
    """发送请求数据"""
    def send_request(self, s, api_data):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = api_data["method"]
            url = api_data["url"]

            if api_data["params"] == "":
                params = None
            else:
                params = eval(api_data["params"])

            if api_data["headers"] == "":
                headers = None
            else:
                headers = eval(api_data["headers"])

            if api_data["body"] == "":
                body_data = None
            else:
                body_data = api_data["body"]

            data_type = api_data["type"]
            if data_type == "data":
                body = eval(body_data)
            elif data_type == "json":
                body = body_data
            else:
                body = params

            # 发送请求
            if data_type == "json":
                headers['Content-Type'] = 'application/json;charset=UTF-8'
                re = s.request(method=method, url=url, headers=headers, data=body.encode('utf-8'))
            else:
                re = s.request(method=method, url=url, headers=headers, data=body)
            return re
        except Exception as e:
            print(e)
