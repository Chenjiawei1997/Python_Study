# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/19 15:21


def f(*args, **kwargs):
    print("收到参数", args, kwargs)
    return True


def call(*args, **kwargs):
    first = None
    if args:
        first = args[0]
    elif kwargs:  # 有关键参数，处理关键字参数
        first_key = list(kwargs)[0]
        first = kwargs[first_key]
    else:  # 没有关键字参数，不进行处理
        pass

    if callable(first):  # 判断是否可以调用
        return first(*args, **kwargs)


# print(call(f,1,2,3,4,5))
# print(call(a=f, b=1, c=3, d=4))
print(call(b=1, c=3, d=4))
