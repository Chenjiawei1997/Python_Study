# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/12 20:19
# key -value 映射结构，简称 k-v 结构

"""
字典决定：
    key -value 映射结构，简称 k-v 结构
    key 必须无歧义，可哈希（可hash）


"""
# 创建字典：
# 字典的创建方式
"""
使用符号 {} 大括号
a = {"a":1,"b":2,"c":3}
内置函数dict,使用内置函数可以不写等于
"""
a = {"a":1,"b":2,"c":3}
print(a)

a = dict(a=1, b=2, c=3)
print(a)


# 修改
"""
增加成员
修改成员
删除成员

d = {}

d["a"] = 1  # 增加成员
d["a"] = 3  # 修改成员
del d["a"]  # 删除成员
print(d)  # 读取成员，key不在，抛异常



字典使用key来访问元素，key具有无歧义的唯一性

字典的添加、删除成员的方法：
    update  修改字典内容
    setdefault 如果key不在，创建有默认值的key
    
字典的删除成员方法：
    pop 移除指定的键值对
    popitem 移除最后的键值对
    clear 移除全部的键值对

"""
# 使用
a = {"b":2,"c":3}
print(a)
a.update(a = "cjw")
a.setdefault("d","safsad")  # a 存在不生效  setdefault 如果key不在，创建有默认值的key
print(a)

# 使用pop
d = {"b":2,"c":3}
d.pop("b")
print(d)

d = {"b":2,"c":3}
print("移除了数据：", d.pop("b"))
print("移除了键值对：", d.popitem())
print(d)


# 使用
"""
优势：
    集中在 使用的方式  
    
index 查找x首次出现的位置
count 查找x 出现的次数

"""

a = {"b": 2, "c": 3}
print(a.get("b"))  # 自带检查键值对是否存在
print("字典里所有的key：", a.keys())
print("字典里所有的value：", a.values())
print("字典里所有的键值对：", a.items())

"""
字典里所有的key： dict_keys(['b', 'c'])
字典里所有的value： dict_values([2, 3])
字典里所有的键值对： dict_items([('b', 2), ('c', 3)])
----- 这里返回的不是列表，而是（映射）
"""

# l = list(a)  # 转为列表
# print(l)

d = {}

d["a"] = 1  # 增加成员
d["a"] = 3  # 修改成员
del d["a"]  # 删除成员
print(d)  # 读取成员，key不在，抛异常
