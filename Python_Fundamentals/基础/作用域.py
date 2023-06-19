# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/1 9:53

# 资料
# https://realpython.com/python-scope-legb-rule/#understanding-scope


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

# 实例
def scope_test():
    spam = "我是 test_spam"  # 变量spam

    def do_local():  # 局部赋值
        spam = "我是本地绑定作用域local_spam"

    def do_nonlocal():  # 函数嵌套赋值，将spam定义为不是本地、不是局部变量，为自定义变量，它会保留定义函数时变量的绑定，当定义变量的作用域不可以用了，那些绑定仍然可以被调用。
        nonlocal spam   # nonlocal 关键字为：声明的变量不是局部变量, 也不是全局变量, 而是外部嵌套函数内的变量。
        spam = "我是自由变量绑定的作用域 nonlocal_spam"

    def do_global():
        global spam   # 全局赋值
        spam = "我是全局绑定作用域global_spam"

    do_local()
    print("局部作用域赋值（默认状态）不会改变scope_test 对spam的绑定作用域:   ", spam)
    do_nonlocal()
    print("函数嵌套赋值对scope_test对spam作用域的赋值:   ", spam)
    do_global()
    print("全局作用域赋值会改变模块层级的绑定:   ", spam)

scope_test()
print("这里的spam是全局没有赋值前的变量，他改变了模块层级的绑定:   ", spam)
