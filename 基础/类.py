# -*- coding: utf-8 -*-            
# @Author : Chen_jia_wei
# @Time : 2023/6/2 14:51
# class leiA():
#     var1 = 100
#     var2 = 200
#
#     def funB(self):
#         print("不使用类属性")
#
#     @classmethod
#     def hanshu1(cls):
#         print(cls.var1, cls.__name__)
#         print(cls.var2)
#
# leiA.hanshu1()
""""
# 使用外部参数
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(a))
class math1():
    def fun1(a):
         for i in a:
             print(i)

math1.fun1(a)

"""
"""
# 使用内部参数
class math1():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    @classmethod
    def fun1(cls):
         for i in cls.a:
             print(i)

math1.fun1()

"""

# # 使用内部参数
# class math1():
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     @classmethod
#     def fun1(cls):
#          for i in cls.a:
#              print(i)
#
# math1.fun1()

# 同时使用内部和外部参数
#
# class math1():
#     dasa = ['a','sada', '安抚', '是梵蒂冈']
#     print(type(dasa))
#     @classmethod
#     def fun1(cls,n):
#         print("给a的参数$s: " %n)
#         for i in cls.dasa:
#             print(i)
#
#
# math1.fun1('n')


"""
如果我们建一dog，那我们建的这个dog 不是特指哪一只，而是所有的dog，
dog 会跑会跳，大多数dog 都会，那我们dog 类要包含他们

"""


#
# class dog():
#
#     def __init__(self, name, age):
#         """
#         :param name: __init__
#                      self
#         :param age: __init__():这是一个特殊方法，每次dog类创建新实例时，会自动运行他
#                                 为什么init旁边加__ init __ 这是一种约定，这是为了避免默认方法与普通方法名称发生冲突
#                      self:    self是指形参，为什么要有这个self呢，是为了python 调用这个方法来创建dog类，将自动传入实参self
#                             每个与实例相关联的方法调用都将传递实参self，他是一个指向实例本身的引用，让实例能够访问类中的属性和方法
#         """
#         self.name = name
#         self.age = age
#         """
#         :param name: self.name = name 前缀为什么要加self？
#         :param age: 定义变量都有前缀slef，已self为前缀可供类中的【所有方法】使用，可以通过类的任何实例来访问
#                     self.name = name 获取与形参 name 相关联的值，并将其赋给变量 name，
#                      然后该变量被关联到当前创建的实例。self.age = age 的作用与此类似。像这样可通过实例访问的变量称为属性。
#         """
#
#     def sit(self):
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over")
#
#
# my_dog = dog('black',110)
# print(f"我的狗的name {my_dog.name}")
# print(f"我的狗的age {my_dog.age}")
# my_dog.sit()
# my_dog.roll_over()

# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         '''描述餐馆'''
#         print("This restaurant's type is " + self.cuisine_type + " . ")
#         print("This restaurant's name is " + self.restaurant_name.title() + ".")
#
#     def open_restautant(self):
#         '''餐馆营业提醒'''
#         print("Welcom our" + self.cuisine_type + " " + self.restaurant_name + " restaurant !")
#
#
# restaurant_1 = Restaurant("radasf","asdaf")
# # restaurant_2 = Restaurant("dsadfasdasd","asfdfsaf")
# # restaurant_3 = Restaurant("22222222","111111111")
# restaurant_1.describe_restaurant()
# # restaurant_2.describe_restaurant()
# # restaurant_3.describe_restaurant()
# # restaurant_1.open_restautant()

#
# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     a = ["asd", "aaa"]
#
#     def describe_user(self):
#         print("用户姓名:" + self.first_name + self.last_name)
#     @classmethod
#     def sad(cls):
#         print(cls.a,cls.__name__)
#
#
#     def greet_user(self):
#         print("你好")
#
#
# user1 = User("阿萨德", "阿萨德")
#
# user1.describe_user()
# user1.greet_user()
# user1.sad()













