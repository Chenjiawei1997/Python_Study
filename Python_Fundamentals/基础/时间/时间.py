# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/19 14:57

import time

print("获取时间", time.time())  # 时间戳 ，秒数
print("年月日时间", time.localtime(time.time()))  # 标准时间，不是字符串
print('-' * 150)
print("时间字符串", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
print("字符转时间", time.strptime("2023-06-19 15:04:59", "%Y-%m-%d %H:%M:%S"))
print('-' * 150)




import datetime

now = datetime.datetime.now()
print("此时此刻", now)
print("此时此刻时间戳", now.timestamp())
print('-' * 150)
print("今天日期", datetime.datetime.today().date())
print("今天日期标准时间", datetime.datetime.today().date().timetuple())
print('-' * 150)






