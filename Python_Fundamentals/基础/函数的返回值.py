# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/19 9:29
# def fun():
#     # return "cjw"
#     return "aaa", "sad", "发送"
#
#
# print(fun())
#
# # 函数不写返回值，返回默认None
# # 函数执行了关键字，执行完毕
#
# cjw = fun
# print(cjw)
# print(cjw())


def fun(*args, **kwargs):
    def add(a, b):
        return a + b
    return add


cjw = fun()
print(cjw(1, 2))























