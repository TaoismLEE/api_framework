# _*_ coding:utf-8 _*_

import time
from lib.mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))
# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))


# 初始化测试数据
datas = {
    # 表记录数据
    '表名1':[
        {'id': 1, 'name': 'Harry', '`limit`': 2000, 'status': 1, 'address': 'CQ', 'start_time': future_time},
        # 字典形式维护记录数据
    ],
    # 表记录数据
    '表名2':[
        {'id': 1, 'name': 'Tom Cat', 'phone': 13511886601, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1},
        # 字典形式维护记录数据
    ],
}


# 初始化测试数据插入表
def init_data():
    DB().init_data(datas)
