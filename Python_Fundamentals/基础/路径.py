# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/19 10:42

from pathlib import Path

# path_1 = Path("路径.py")
# path_2 = Path("路径.py")
# path_3 = Path("../../路径.py")
# # E:\Python_Study\Python_Fundamentals\基础\路径.py
# print(path_1.absolute())
# print('*' * 50)
# print("文件的名字 ", path_1.name)
# print("文件的后缀扩展名： ", path_1.suffix, path_1.stem)
# print("文件的位置： ", path_1.parent.absolute())
# print('*' * 50)
# print("文件的内容： ", path_1.read_text(encoding='utf-8'))
# print('*' * 50)


"""
open 

位置参数
file ： 文件的路径（相对路径/绝对路径）
关键字参数
mode： 打开模式
encoding： 文本编辑
    gbk
    utf-8
"""
# 1/文件路径
path = '路径.py'
f = open(path)
print(f)









