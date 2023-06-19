# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/19 15:37

"""
类
程序 = 数据结构 + 算法
通过函数 封装数据和算法



"""

import aaa  # 命名空间

# class Fun:
#     n = 0
#
#     def f(self):
#         self.n = self.n + 1
#         return self.n
#
#
# a = Fun()  # 实例对象 会创建新的命名空间
#
# print(a.f())
# print(a.f())

# fun_1 = Fun()  # 对类进行实例化，得到了实例对象
# fun_1.n = 111
# print(fun_1.n)  # 访问命名空间的 变量
# print(fun_1.f(B))  # 访问命名空间的  函数

# 传什么参数 给f？
# 1/拥有命名空间
# 2/命名空间有n

"""
类是如何实现数据隔离的，是闭包作用域嘛？
1/ 外部可以修改函数


类中的数据，和实例中的数据，是什么关系

1/访问实例数据时，会先从实例中的ns中寻找，如果没有，就从类的ns中寻找

"""

# class A:
#     name = "123"
#
#     def show(self):
#         print(self, type(self))
#         print(self.name)
#
#
# # 1/ A.show(A)   # 把classA传递给self，那么self 就是class A
#
# a = A()  # 实例化之后
# # a.show()  # 把实例a 传递给slef， 那么self 就是实例 a


# 2/ 面向对象的角度

# a.show()  # 没有传递参数，但是实例会自动传参，自动传参，传递的就是这个实例自己 这个名字叫self  实例自己

import time

# with open("a.txt", "wt") as f:
#     f.write("2023-06-19 20:12:00")
#
# with open("a.txt", "rt") as f:
#     txt = f.read()
#
# # 此时文件自动关闭，但是变量还可以使用
# print(txt)
#
# # 这边进行了计算
# t = time.strptime(
#     txt, "%Y-%m-%d %H:%M:%S",
# )
# print(time.mktime(t))


class Timer:

    def __init__(self, file, time_str):
        self.file = file
        self.time_str = time_str

    def to_txt(self):
        with open("a.txt", "wt") as f:
            f.write(self.time_str)

    def to_timestamp(self):
        with open(self.file, "rt") as f:
            txt = f.read()
            t = time.strptime(
                txt, "%Y-%m-%d %H:%M:%S",
            )
        return time.mktime(t)


t = Timer("a.txt", "2023-06-19 20:12:11")
# 1
print(t.to_txt())

#2
print(t.to_timestamp())