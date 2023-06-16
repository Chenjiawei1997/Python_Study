# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/16 19:16

"""
函数(签名)
    名字
    参数
    返回值


"""


# # 位置参数
# def add(a: int, b: int) -> int:
#     c = a + b
#     return c
#
#
# res = add(1, 2)  # 对函数的调用(call),使用函数
# print(res)
#
#
# # 关键字参数
# def add(a: int, b: int) -> int:
#     c = a - b
#     return c
#
#
# res = add(b=5, a=1)  # 对函数的调用(call),使用函数
# print(res)


# def add(f: str, a: int, b: int) -> int:
#     if f == "+":
#         c = a + b
#     else:
#         c = a - b
#     return c
#
#
# res = add("+", b=2, a=1)  # 对函数的调用(call),使用函数
# print(res)

# 默认参数
def add(f: str, a: int, b: int = 0) -> int:
    if f == "+":
        c = a + b
    else:
        c = a - b
    return c


res = add("+", 2, 9)  # 对函数的调用(call),使用函数
print(res)


# 不定长参数






# 函数的参数
"""
位置 在前，关键字在后
位置参数:   通过参数的位置,来决定名字的参数
 res = add(1, 2)
 
关键字参数:  通过关键字来决定名字的参数
res = add(b=5,a=1)

默认参数:


不定长参数:  


"""
