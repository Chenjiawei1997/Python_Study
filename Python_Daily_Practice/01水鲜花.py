# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/9 14:40
# python 每日一练
print("水仙花从100到1000")
for i in range(100, 1000):
    # 加入一个数是371  取整除取百位371//100 = 3
    x = i // 100
    # 取一个数字十位，371//10=3 7 ，37%10=7  除数余7
    b = i // 10 % 10
    # 除数取余个位
    c = i % 10
    # 判断 个 十 百 三次方 是否等于它本身，如果是就是水仙花数。
    if x ** 3 + b ** 3 + c ** 3 == i:
        print(f'{i}是水仙花数')


"""
range 函数
    # Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型
    # range(start, stop[, step])
    # 参数说明：
    # start：计数从start 开始。默认是从0开始。例如range (5) 等价于range (0，5) ;
    # stop：计数到stop结束，但不包括stop。 例如: range (0，5) 是 [0, 1, 2, 3, 4]没有5
    # step：步长，默认为1。例如: range (0， 5) 等价于 range(0, 5, 1)
    # range(5, 0, -1): [5, 4, 3, 2, 1]
"""