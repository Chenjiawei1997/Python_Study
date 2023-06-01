# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/1 13:42


"""
高阶函数
    一个函数的参数，可以是另外一个或者几个函数

"""
# 高阶函数
def a():
    print("我是函数a")

def b(c):
    print("start".center(20, "="))
    c()
    print("end".center(20, "="))

b(a)
# b的参数是一个函数a