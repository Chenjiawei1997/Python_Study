# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/10 14:38
"""
输入年月日，输出该日期是否是闰年，并且输出该日期是此年份的第几天

闰年判断条件（两个条件满足任意一个就为闰年）:

一、能被4整除，并且不能被100整除
二、能被400整除

"""

# 接收用户输入的年月日，创建保存12个月的天数列表
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
# 创建12个月的天数列表
date_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 用来统计第几天
count_day = day

# 2、根据年份判断是否是闰年，如果是把 二月份设为 29 天，否则把二月份设为 28 天
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%s 年是闰年" % year)
    date_list[1] = 29
