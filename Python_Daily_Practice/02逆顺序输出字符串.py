# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/9 14:41
"""
    输入一个字符串然后对其进行逆序输出

    第一种方式：字符串切片
    第二种方式：使用循环转换然后逆序输出
    比如：输入字符串'hello'，逆向输出'olleh'
"""
print("第一种切片方式")
str_info = input("请输入字符：")
print("逆序输出：", str_info[::-1])

# 第二种是循环索引下标 需要用到range() 函数
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
# print("第二种索引下标方式")
str_info1 = input("请输入字符：")
# 为什么定义一个空列表   1、将下标索引到的数据放到这个空列表当中
str_info1_list = []
# 开始处理循环
for i in range(len(str_info1) - 1, -1, -1):
    '''
    len(str_info1) - 1 ： 这个是根据你输入的字符串取最大索引位置，你输入hello  hello取到的值是4
    第1个 -1  ：  就是结尾，左闭右开 那就是hello 中的 o
    第二个 -1  ： 倒序的意思
    '''
    # append 是添加函数
    str_info1_list.append(str_info1[i])

print("索引下标放到的空列表str_info1_list", str_info1_list)
# 索引下标（hello）索引下标后每个字符['o', 'l', 'l', 'e', 'h']
print("逆顺序输出1：", ''.join(str_info1_list))
# 然后转换成字符串olleh
