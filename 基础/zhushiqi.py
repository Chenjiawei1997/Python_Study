# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/1 20:05

from 装饰器 import timer
import time


@timer
def fun1():
    time.sleep(1)
print(fun1.__name__)
fun1()

