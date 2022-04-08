# def input_list(my_list):
#     if len(my_list) != len(set(my_list)):
#         return True
#
#
# num = [1, 2, 3, 1]
# print(input_list(num))

# name = "Alex"
# if name.startswith("Al"):
#     print("True")
# else:
#     print("False")

# flag = name.startswith("Alex")
#
# if flag:
#     print("True")
# else:
#     print("False")


# def name_start(input_name):
#     flag = input_name.startswith("Al")
#     if flag:
#         return True
#     else:
#         return False
#
#
# print(name_start("Jl"))
# print(name_start("Alex"))
#
# name = "Allex"
# print(name.find("l"))
# print(name.rfind("l"))

# name = "Alex"
#
# print("_".join(name))

# n1 = 0
# n2 = 1
# n3 = n1 + n2

# Fibonacci sequence
# n1, n2 = 0, 1
#
# i = 0
# while i < 7:
#     print(n1)
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     i +=1


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield a
#         a, b = b, a + b
#         n = n + 1
#
# for i in fib(7):
#     print(i)
# tuple1 = (1,2, 4)
# a, b, c = tuple1
# print(a, b, c)
#
# def is_leap(year):
#     if year % 4 ==0 and year % 100 ==0 and year% 400 ==0:
#         return True
#     elif year % 4 ==0 and year % 100 != 0:
#         return True
#     else:
#         return False
#
#
# print(is_leap(2017))
# print(is_leap(1900))
# print(is_leap(2012))
# print(is_leap(2000))

# def rever_str(str):
#     print(str[::-1])
#
#
# rever_str("Alex")
#
# def rever_str(str):
#   i = len(str)
#   new_str=""
#   while i >0:
#       new_str+=str[i-1]
#       i -=1
#   print(new_str)
#
# rever_str("Alex")

# my_list = [1,2, 3, 4,5]
#
# for i, v in enumerate(my_list):
#     print(v)

# name = "Alex"
#
# new_name = ""
#
# for i in name:
#     if i == name[2]:
#         continue
#     else:
#         new_name += i
# print(new_name)
from practice1 import my_list

# my_tuple = {1, 3, 4}
# my_tuple.add(2)
# print(my_tuple)


