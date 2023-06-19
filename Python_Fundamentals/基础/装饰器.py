# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/30 16:50
"""
装饰器（decorator）也称装饰函数，是一种闭包的应用
其主要是用于某些函数需要拓展功能，但又不希望修改原函数，它就是语法糖，
使用它可以简化代码、增强其可读性，当然装饰器不是必须要求被使用的，不使用也是可以的，Python 中装饰器通过 @ 符号来进行标识。

在python中，装饰器的本质就是一个高阶函数，它接受一个函数作为参数，并返回一个被装饰后的函数。

装饰器的作用如下：
    在不修改被装饰函数的源代码和调用方式的情况下，给被装饰函数添加额外的功能。
    即就是你传一个函数给装饰器，装饰器不会改变该函数的代码和调用方式就能使该函数获得额外的功能。

要懂装饰器得提前需要了解两个知识点：
1、什么是高阶函数
    高阶函数
    一个函数的参数，可以是另外一个或者几个函数
2、什么是闭包
    闭包是一种函数，一种延伸了变量作用域的函数，它会保留定义函数时变量的绑定，当定义变量的作用域不可以用了，那些绑定仍然可以被调用。
3、才懂什么是装饰器
    装饰器的本质就是一个高阶函数，它接受一个函数作为参数，并返回一个被装饰后的函数。
    在不修改被装饰函数的源代码和调用方式的情况下，给被装饰函数添加额外的功能。
"""
"""
import time
def fun():
    time.sleep(2)
def timer(funB):
    start_time = time.time()
    funB()
    end_time = time.time()
    total = end_time - start_time
    print("函数运行的时间为：{}".format(total))
timer(fun)
# 这里每次计算函数运行的时候就要调用一次timer 函数，如果函数有几百个，就得调用几十次，几百次timer函数，不太乐观

"""
"""
import time
def fun():
    time.sleep(2)
def timer(fun):
    def wrapper():   # 函数嵌套 wrapper
        start_time = time.time()
        fun()
        end_time = time.time()
        total = end_time - start_time
        print("函数运行的时间为：{}".format(total))
    return wrapper
# timer 返回函数嵌套 wrapper
# fun1 = wrapper
fun1 = timer(fun)
# 调用fun1 就是调用 wrapper()函数
fun1()

"""
"""
import time

def timer(fun):
    def wrapper():   # 函数嵌套 wrapper
        start_time = time.time()
        fun()
        end_time = time.time()
        total = end_time - start_time
        print("函数运行的时间为：{}".format(total))
    return wrapper

@timer
def fun():
    time.sleep(2)

fun()

"""

import time
import functools

# def timer(fun):
#     print("我是老6")
#     @functools.wraps(fun)
#     def wrapper():   # 函数嵌套 wrapper
#         start_time = time.time()
#         fun()
#         end_time = time.time()
#         total = end_time - start_time
#         print("函数运行的时间为：{}".format(total))
#     return wrapper
#
# @timer
# # @timer 和 fun =timer(fun) 一样
# def fun():
#     time.sleep(2)
# print(fun.__name__)
#
# if __name__ =='__main__':
#     fun()
#     print(__name__)
# # fun()


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
# # 业务函数
# @funA
# def funC(name):
#     print("hello:", name)
#
# funC('无敌小手')

# 接受参数的装饰器
# 装饰函数

import time
import functools
def funC():
    time.sleep(2)

def funA(funC):
    # @functools.wraps(funC)
    def funD():
        strat_time = time.time()
        funC()
        end_time = time.time()
        total = end_time - strat_time
        print("时间：{}".format(total))
    return funD

fun1 = funA(funC)
fun1()
print(funC.__name__)
# def funA(flag):
#     def funB(fun):
#         def funC(*args, **kwargs):
#             if flag == True:
#                 print("名字是正确的")
#             elif flag == False:
#                 print("名字是错误的")
#
#         return funC
#
#     return funB
#
#
# @funA(True)
# def funD(name):
#     print('hello', name)
#
#
# funD()

# 基于类 实现
# class Test(object):
#     def __init__(self, func):
#         print('函数名是 %s ' % func.__name__)
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         self.__func()

# @Test
# def hello():
#     print('Hello ...')
# hello()

"""
类装饰器
"""

# # 类装饰器
# import time
#
#
# class timer():
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         star_time = time.time()
#         self.func()
#         end_time = time.time()
#         total = end_time - star_time
#         print("函数运行时间：", total)
#
#
# @timer
# def fun():
#     time.sleep(2)
#
#
# fun()

"""
类装饰器使用__call__ 方法实现的
    能够使类的实例像函数调用那样被调用
    @timer等价于 fun=timer(fun)
@timer 的在这里的作用实际就是实例化一个fun对象（fun=timer(fun)），
对于类的实例化对象是不支持** 实例化对象() 
**这样调用的，而__call__ 方法的作用就是支持实例化对象这样被调用。所以才满足装饰器不改变被装饰函数调用方式的特性。


"""
