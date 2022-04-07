# list_1 = [[54, 28, 88, 99, 77],[99, 6, 37, 68, 83],[90, 52, 36, 4, 53],[85, 66, 11, 11, 61],[20, 52, 9, 81, 61],[23, 67, 37, 39, 18],[21, 36, 66, 80, 30],[74, 80, 5, 7, 96],[30, 35, 71, 73, 4],[40, 67, 67, 11, 71]]
#
# # Please your code here
# new_list = []
# for item in list_1:
# 	max_num = max(item)
# 	new_list.append(max_num)
# ave_list = sum(new_list)/len(new_list)
# print(ave_list)
#
# round(84.1, 3)

# name = "Jim"
# age = 35
#
# # 传入参数
# print("my name is {} and age is {}".format(name, age))
# print("my name is {0} and age is {1}".format(name, age))
# print("my name is {name} and age is {age}".format(name="jim", age=35))
#
# #f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
# tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
# print(tpl)
#
# #f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
# tpl = "i am {:s}, age {:d}, money {:.2f}".format("seven", 18, 88888.1)
# print(tpl)

# list_1 = ['jiu', 'zhangyu', 'luosifen']
#
#
# list_2 = []
# for item in list_1:
# 	list_item = list(item)
# 	print(list_item)
# 	if list_item[0] in ["j", "z", "d", "f", "h"]:
# 		list_2.append(item)
#
# a = "jiu"
# a.split()
# print(a)

# def print_avg(*args, **kwargs) -> str:
#     # Please write your code here
#     print(kwargs)
#     print(args)
#
# print_avg(1, 2, 3, name="Jim")
# from statistics import mean
#
# list1 = [1, 2, 3, 4, 5]
# print(mean(list1))
# for i in range(100, 201):
# 	if i % 2 !=0 and i % 3 !=0:
# 		print(i)
#
# for i in range(2, 101):
#     is_prime = True
#     for x in range(2, i):
#         if i % x == 0:
#             is_prime = False
#     if is_prime:
#         print(i)
#
#
# def is_prime(m):
#     prime = True
#     for i in range(2, m):
#         if m % i == 0:
#             prime = False
#     if prime:
#         return m
#     else:
#         return "not prime"
#
#
# print(is_prime(75))

my_list = [5,4,3]
# for i in my_list:
# 	for n in my_list[1:]:
# 		for m in my_list[2:]:
# 			if i **2 + n **2 == m **2:
# 				print("True")
#

#
# def input_list(my_list):
# 	my_list.sort()
# 	for i in my_list:
# 		for n in my_list[1:]:
# 			for m in my_list[2:]:
# 				if i ** 2 + n ** 2 == m ** 2:
# 					return True
# 	return False
#
# print(input_list(my_list))
# def input_number(num):
# 	for i in range(0, num + 1 ):
# 		if i % 3 == 0 and i % 5 ==0:
# 			print("FizzBuzz")
# 		elif i % 3 == 0:
# 			print("Fizz")
# 		elif i % 5 == 0:
# 			print("Buzz")
# 		else:
# 			print(i)
#
# input_number(15)
#
# print(0%3)

# def rotate(l, k):
#   for i in range(k):
#     l.insert(0, l.pop())
#   r
#   eturn l
#
# # print(rotate([1,2,3],1))
# list1=["a", "b", "c"]
# list1.pop()
# print(list1)
#
# list3=[0,1,4,]


# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(sqs[::-1])

