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

name = "Jim"
age = 35

# 传入参数
print("my name is {} and age is {}".format(name, age))
print("my name is {0} and age is {1}".format(name, age))
print("my name is {name} and age is {age}".format(name="jim", age=35))

#f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
print(tpl)

#f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
tpl = "i am {:s}, age {:d}, money {:.2f}".format("seven", 18, 88888.1)
print(tpl)

