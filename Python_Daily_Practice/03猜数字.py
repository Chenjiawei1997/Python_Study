# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/5/9 14:41

"""
    需求描述：
        随机生成一个100以内的整数，共有10次机会开始游戏，输入猜测的数字
        如果猜小了，提示猜小了
        如果猜大了，提示猜大了
        猜对了，提示猜对了，并且结束游戏
        10次机会用完还没猜对，提示游戏结束，没有猜到。

"""
# print("10次机会猜大小")
# import random
# # 导包
# number = random.randint(0, 100)
# # 随机一个数字0-100  左开右闭
# for i in range(10):
#     choice = int(input("请输入你要猜的数字： "))
#     if choice > number:
#         print("你猜大了")
#     elif choice < number:
#         print("你猜小了")
#     else:
#         print("你猜对了")
#         print(f"一共用了{i + 1}机会")
#         break
#     print(f"还剩下{9 - i}机会")
# else:
#     print("游戏结束你还没有猜到")


print("不限机会猜大小")
import random
# 导包
number = random.randint(0, 100)
# 随机一个数字0-100  左开右闭
# 定义机会为count = 0
count = 0
while True:
    # 每循环一次加1
    count += 1
    choice = int(input("请输入你要猜的数字： "))
    if choice > number:
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了")
        print(f"一共用了{count}机会")
        break

