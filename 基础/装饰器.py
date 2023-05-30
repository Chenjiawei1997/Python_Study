# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/30 16:50

# 装饰器（decorator）也称装饰函数，是一种闭包的应用，其主要是用于某些函数需要拓展功能，但又不希望修改原函数，它就是语法糖，
# 使用它可以简化代码、增强其可读性，当然装饰器不是必须要求被使用的，不使用也是可以的，Python 中装饰器通过 @ 符号来进行标识。
# 装饰器可以基于函数实现也可基于类实现，其使用方式基本是固定的，看一下基本步骤：

# 定义装饰函数（类）
# 定义业务函数
# 在业务函数上添加 @装饰函数（类）名


# 接下来通过示例来作进一步了解。

# 装饰器函数
# def funA(fun):
#     def funB(*args, **kwargs):
#         print("函数 " + fun.__name__ + "开始执行")
#         fun(*args, **kwargs)
#         print("函数 " + fun.__name__ + "执行结束")
#
#     return funB
#
#
# # 业务函数
# @funA
# def funC(name):
#     print("hello:", name)
#
# funC('无敌小手')

# 装饰函数
