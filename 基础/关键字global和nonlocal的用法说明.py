# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/1 10:46

# 关键字global和nonlocal的用法说明
"""
global 关键字是用来函数 和 其他作用域中使用的全局变量

"""
"""
1/局部变量 修改 全局变量 不使用 global 关键字会报错

count = 0  # 定义全局变量count 让他初始为 0
def global_test():  #定义global_test 函数名
    count += 1      # 局部变量 count 自增 1
    print(count)    # 输出 count
global_test()       # 调用 global_test 函数
会报错 ：UnboundLocalError: local variable 'count' referenced before assignment
"""

"""
2/局部变量 修改 全局变量 ，应该在局部变量中声明全局变量，这样才不会报错

count = 0  # 定义全局变量count 让他初始为 0
def global_test():  # 定义global_test 函数名
    global count    # 局部 函数 global_test内 声明全局变量
    count += 1      # 局部变量 count 自增 1
    print(count)    # 输出 count
global_test()  # 调用 global_test 函数
print(count)
"""
"""
定义一个变量 不是局部变量/全局变量/不做修改 ，调用函数输出正常

count = 0  # 定义变量count 让他初始为 0
def global_test():  # 定义global_test 函数名
    print(count)  # 输出 count
global_test()  # 调用 global_test 函数
"""
"""
nonlocal  解释为 非局部的 
nonlocal 关键字为：声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。

"""

#
# def nonlocal_test():
#     count = 0
#
#     def test2():
#         nonlocal count
#         # global count
#         # 在嵌套内的函数中 ， 如果你使用了 global 就会发生报错
#         # 报错为：NameError: name 'count' is not defined  意思是 count不在本地定义中，也不是全局定义 找不到这个count 这个变量
#         # nonlocal 就是把这个count进行标记，告诉这个test2()这个函数 count 既不是本地，也不是全局，count 为自由变量
#         count += 1
#         return count
#
#     return test2
#
# val = nonlocal_test()
# print(val())
# print(val())
# print(val())
# print(val())
# print(val())
"""
def f():                     # 定义函数 f（）
    count = 0                # 定义变量count 为0 ，他的作用域 在fu（） 函数中为局部变量 

    def a():                 # 定义嵌套函数为a（）  嵌套函数a 中 就是闭包作用域
        nonlocal count       # 将a（）函数中的 count 告诉a（） 他不是全局变量 也不是本地变量
        count += 1           # count 自增 1
        print(count)         # 输出count
    return a()               # a（）函数 返回a的方法 
    # return a               # a  函数a 不加（） 返回的是一个a的内存地址

f() 

代码注释连起来看他做了哪些事情：
1、调用函数f时，f会返回a（）
2、当执行a（）的时候，f函数的任务已经完成了，它占用的资源就会释放掉，这其中包括了函数f环境中定义的count变量。
3、在执行a的时候，函数f进行了释放，没有办法再去找到其中的数据。
4、像函数a中count这一类，不在本地定义域中绑定的变量，我们叫做自由变量。
5、用nonlocal标记后呢，Python就会保留自由变量的绑定（或者说定义环境）。
6、整个函数a的作用域是“count = 0”，加上a本身。
总结：a延伸了自己的作用域，这里就可以被称作“闭包”。书面意思讲解：调用一个函数X返回值一个函数y 叫闭包
"""

"""
我们学到了什么？
global / nonlocal 就是指 改变变量的作用域
global标记为 全局变量， nonlocal标记为 非全局，非本地的“自由变量”
延时作用域的函数，叫做闭包

"""
"""
作用域 又称 命名空间，指变量起作用的范围。
Python变量作用域可以分为四种，
分别为：
1、局部作用域（Local、简称 L）
2、嵌套作用域（Enclosed，简称 E）
3、全局作用域（Global，简称 G）
4、内置作用域（Built-in，简称 B）
*调用顺序为就近原则，LEGB
"""


# def f():  # 定义函数 f（）
#     count = 0  # 定义变量count 为0 ，他的作用域 在fu（） 函数中为局部变量
#
#     def a():  # 定义嵌套函数为a（）  嵌套函数a 中 就是闭包作用域
#         nonlocal count  # 将a（）函数中的 count 告诉a（） 他不是全局变量 也不是本地变量
#         count += 1  # count 自增 1
#         # print(count)  # 输出count
#
#     print("判断是否为闭包", a.__closure__)
#     return a()
#     # a（）函数 返回a的方法
#     # return a               # a  函数a 不加（） 返回的是一个a的内存地址
#
#
# f()


def funA():
    c