# encoding: utf-8
# Author: 陈家伟


"""
数据类型

"""

"""
常用的数据类型

整数类型 ----> int
浮点-----> float
布尔-----> bool------> True/false
字符串-----> str 

"""

"""
存储类型 有四种
元组、列表、字典、集合
元组
1、什么是元组？
元组是有序的且不可更改的集合 用 （） 表示,元组的元素无法修改
tuple_name = (1,'element_1',"2#*")
2、元组中的元素？
元素内的元素得是字符串，数字； 当元组中只包含一个元素时候，需要在元素后面添加逗号，不然会被当做运算符使用
tuple_name = (1,)


列表
列表的元素可以修改使用 [] 来表示

3、下标索引方式：
元组和列表一样，可以使用下标索引访问元组中的某个元素（得到一个元素的值），也可以切片访问元组中的一组元素（一组子元组）
下标索引分正向索引，反向索引
tuple_name = (1, 2, 3, 4, 5)
print(tuple_name[1]) #正向索引
print(tuple_name[-1])# 反向索引
切片访问：
元组值     1   2   3   4   5  6
正向索引   0   1   2   3   4  5
方向索引  -6  -5  -4  -3  -2 -1
表达式：tuple_name = (start：end：step)  
start：表示起始索引
end：结束索引
step：表示步长
使用表示式：tuple_name = (start：end)   是左闭右开区间，访问不了end的元素 

检查元组是否存在，可以使用 关键字 in 来判断 
tuple_name = (1, 2, 3, 4, 5,6)
print(2 in tuple_name)

"""
# tuple_name = (1, 2, 3, 4, 5,6)
# print(tuple_name)
# for i in tuple_name:
#     print(i)

# tuple_name[0] = 99

# print(2 in tuple_name)
# print(tuple_name[1])
# print(tuple_name[-1])
# l = [1,2,3]
# # l.pop(0)
# del l[1]
# print(l)

# 元组的增删改查

# 元组拼接
# tuple_name1 = (1, "aS", "无敌")
# tuple_name2 = (2, "sad", "小手")
# print(tuple_name2 *2)
# # 元组不变性
# tuple_name = (1, 2, 3, 4, 5,6)
# tuple_name[0] = 99
# print(tuple_name)
# # 代码报错：TypeError: 'tuple' object does not support item assignment

# tup = (1,2,3)
# print(id(tup))
# tup = (4,5,6)
# print(id(tup))


# tuple_name = (1, 2, 3, 4, 5,6)
# print(2 in tuple_name)
#
# tupe = (1,)
# tupe.__add__((2,3))

# # 元组 添加元素
# a = (1,2,3)
# a = list(a)
# print(type(a))
# a.append(8)
# a = tuple(a)
# print(a)
# print(type(a))


# 元组删除元素
# tupe = (1, 2, 3,3, 4,4, 5, 6)
# print(f"原元组{tupe}")
# print(type(tupe))
# tupe = list(tupe)   # 转换列表
# print(type(tupe))
# print(f"转换为列表{tupe}")
# tupe
# print(f"切片列表{tupe}")
# # # 类型转换


# 元组切片
# tupe = (1, 2, 3, 4, 5, 6)
# print(f"原元组{tupe}")
# tupe = tupe[3:]  # 重新赋值
# print(f"切片后{tupe}")
