# my_str = "The brown-eyed man drives a brown car."
# replace_char = "green"
#
# new_str = my_str.replace("brown", replace_char)
# print(new_str)

# def len_str(str):
#     print(len(str))
#
# def string_length(str1):
#     count = 0
#     for char in str1:
#         count += 1
#     return count
# print(string_length('w3resource.com'))

# my_str = "Hello"
# print(my_str.count("l"))


"""
6. Write a Python program to count the number of characters in a string. Go to the editor
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

"""
# def count_str(input_str):
#     dic_str = {}
#     for i in input_str:
#         key = i
#         value = input_str.count(i)
#         dic_str[key] = value
#     print(dic_str)
#
# count_str("google.com")

"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

"""

# def result(input_list):
#     count = 0
#     for item in input_list:
#         if len(item) >=2 and item[0] == item[-1]:
#             count +=1
#     return count
#
# print(result(['abc', 'xyz', 'aba', '1221']))

# alist = [2, 5, 8, 1, 9, 3, 7]
# alist.sort()
# print(alist)

# aTuple = (2, 5, 8, 1, 9, 3, 7)
# result = sorted(aTuple)
# print(result)

# take the second element for sort
# def take_second(elem):
#     return elem[1]
#
#
# # random list
# random = [(2, 2), (3, 2), (4, 1), (1, 3)]
#
# # sort list with key
# sorted_list = sorted(random, key=take_second)
#
# # print list
# print('Sorted list:', sorted_list)

"""
9. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""


def sort_list(input_list):
    result_list = sorted(input_list, key=lambda x: x[-1])
    return result_list


print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

"""
10. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

"""