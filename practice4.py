# # def solution(input_num1, input_num2):
# #     num_sum = int(input_num1) + int(input_num2)
# #     return num_sum
# #
# # num1 = '364'
# # num2 = '1836'
# #
# # # print(solution(num1, num2))
# #
# #
# # def solution(num1, num2):
# #     eval(num1) + eval(num2)
# #     return eval(num1) + eval(num2)
# #
# #
# # print(solution(num1, num2))
# # def solution(input_str):
# #     dic = {}
# #     for i in input_str:
# #         dic[i] = input_str.count(i)
# #     for i in range(len(dic)):
# #         if dic[input_str[i]] == 1:
# #             return i
# #     return -1
# #
# # print(solution('alphabet'))
# # print(solution('barbados'))
# # print(solution('crunchy'))
#
# # print(eval("1+5"))
#
# from collections import Counter
#
# string = "www.google.com.au"
#
# counter = Counter(string)
# # print(counter)
# # dict = dict(counter)
# # print(dict)
# # print(dict.keys())
# # print(dict.values())
# # print(list(counter))
# # print(sorted(counter)) # 去重复
# # print(counter.items())
# # for item in counter.items():
# #     print(item)
# print(counter["g"])
# print(counter.most_common(2))
"""
11.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
"""

# def solution(input_str):
#     first_char = input_str[0]
#     new_str = input_str.replace(first_char, "$")
#     new_str = first_char + new_str[1:]
#
#     return new_str

# print(solution("october"))

"""
12. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

Click me to see the sample solution

"""

# def solution(str1, str2):
#     new_str1 = str2[:2] + str1[2:]
#     new_str2 = str1[:2] + str2[2:]
#     return new_str1 + " " + new_str2
#
# print(solution("abc", "xyz"))

"""
13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

"""


# def solution(input_str):
#     if len(input_str) < 3:
#         return input_str
#     else:
#         if input_str.endswith("ing"):
#             input_str = input_str[:-3] + "ly"
#             return input_str
#         else:
#             return input_str + "ing"
#
# print(solution("am"))

# string = "Hello"
# # string = string[-1:-4]
# # print(string)
# string = enumerate(string)
# print(set(string))

"""
14. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'

"""


# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][1]
#
# print(find_longest_word(["PHP", "Exercises", "Backend"]))


# def is_integer(n):
#   try:
#       n= int(n)
#       print("valid integer :", n)
#   except ValueError as err:
#       print(err)
# is_integer(15)
# is_integer(5.65)
# is_integer('5.65')

# n = "3.1"
# print(n.isdecimal())

# def solution(my_dict):
#     def my_func(element):
#        return element[1]
#
#     my_dict2 = sorted(my_dict.items(), key=my_func, reverse=True)
#     return dict(my_dict2)
#
# def solution(input_dict):
#     new_dict = sorted(input_dict.items(), key=lambda x : x[0] )
#     return dict(new_dict)
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# print(solution(d))

# d = {0:10, 1:20}
# print(d)
# d[2]=30
# print(d)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4)


# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# print(set(a))
#
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
#
# print(dup_items)

# original_list = [10, 22, 44, 23, 4]
# new_list = original_list[:]
# print(id(new_list))
# print(id(original_list))
#
# # new_list = list(original_list)
# # print(original_list)
# # print(new_list)

"""
Write a Python program to remove the nth index character from a non empty string
"""
# def solution(input_str, num):
#     if num <= len(input_str):
#         new_str = input_str[0:num-1] + input_str[num:]
#         return new_str
#
# print(solution("Python", 5))


# def remove_char(str, n):
#     first_part = str[:n]
#     last_pasrt = str[n + 1:]
#     return first_part + last_pasrt
#
#
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))

# def solution(input_str):
#     first_char = input_str[0]
#     last_char = input_str[-1]
#     new_str = last_char + input_str[1:-1] + first_char
#     return new_str
# print(solution("12345"))
#
#
# def change_sring(str1):
#     return str1[-1:] + str1[1:-1] + str1[:1]
#
#
# print(change_sring('abcd'))
# print(change_sring('12345'))

# def solution(input_str):
#     new_str = ""
#     for i in range(len(input_str)):
#         if i % 2 == 0:
#             new_str += input_str[i]
#     return new_str
#
# print(solution('abcdef'))
# print(solution('python'))
#
# def odd_values_string(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result + str[i]
#     return result


# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
sensetance = "The quick brown fox jumps over the lazy dog"

import collections
# my_list = sensetance.split()
#
# counter = collections.Counter(sensetance)
# print(counter)
#
# new_counter = collections.Counter(my_list)
# print(new_counter)
# string = "www.google.com.au"
#
# counter = collections.Counter(string)
# print(counter)
# dict = dict(counter)
# # print(dict)
# # print(dict.keys())
# # print(dict.values())
#
# print(sorted(counter))


# c = collections.Counter('ABCABCCC')
# print(c)
# print(c.elements())  # <itertools.chain object at 0x0000027D94126860>
#
# # 尝试转换为list
# print(list(c.elements()))  # ['A', 'A', 'C', 'C', 'C', 'C', 'B', 'B']
#
# # 或者这种方式
# print(sorted(c.elements()))  # ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C']
#
# # 这里与sorted的作用是： list all unique elements，列出所有唯一元素
# # 例如
# print(sorted(c))  # ['A', 'B', 'C']

# def solution(input_list1, input_list2):
#     new_list = input_list1 + input_list2
#     new_set = set(new_list)
#     if len(new_set) != len(new_list):
#         return True
#     else:
#         return False
# print(solution([1,2,3,4,5], [5,6,7,8,9]))
# print(solution([1,2,3,4,5], [6,7,8,9]))

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{}x{}={}\t'.format(i, j,i*j))
#     print()

# from collections import Counter
# def solution(input_str):
#     c = Counter(input_str).items()
#     print(c)
#     for item in c:
#         if item[1] == 1:
#             return input_str.find(item[0])
#
# print(solution('alphabet'))
# print(solution('www.google.com.au'))
# print(solution('crunchy'))

# string="Hello"
# for i, v in enumerate(string):
#     print(i, v)


# def solution(s):
#     frequency = {}
#     for i in s:
#         if i not in frequency:
#             frequency[i] = 1
#         else:
#             frequency[i] +=1
#     for i in range(len(s)):
#         if frequency[s[i]] == 1:
#             return i
#     return -1
#
# print(solution('alphabet'))
# print(solution('barbados'))
# print(solution('crunchy'))

# def solution(num1):
#     str1 = str(num1)
#     if str1[::-1] == str1:
#         return True
#     else:
#         return False
#
# print(solution(14641))

# def solution(input_list):
#     is_monotonic = False
#     for i in range(len(input_list)):
#         for m in range(1, len(input_list)):
#             if input_list[i] >= input_list[m] or input_list[i] <= input_list[m]:
#                 is_monotonic = True
#     return is_monotonic
#
# print(solution([6, 7, 4, 4] ))


#
# new_A= [for i in range(len(nums) - 1) if nums[i] <= nums[i + 1] ]
# print(new_A)
# print(all(new_A))
# def solution(input_list):
#     new_list = []
#     new_item = 0
#     for item in input_list:
#         if item is not None:
#             new_list.append(item)
#             new_item = item
#         else:
#             new_list.append(new_item)
#     return new_list
#
# input_list = [1,None,2,3,None,None,5,None]
# print(solution(input_list))

"""
#Given two sentences, return an array that has the words that appear in one sentence and not the other and an array with the words in common. 

"""

# def solution(input_str, input_str2):
#     new_list = []
#     common_list = []
#     list1 = input_str.split()
#     list2 = input_str2.split()
#
#     for i in list1:
#         if i not in list2:
#             new_list.append(i)
#         else:
#             common_list.append(i)
#     return new_list, common_list
#
# sentence1 = 'We are really pleased to meet you in our city'
# sentence2 = 'The city was hit by a really heavy storm'
# print(solution(sentence1, sentence2))


print(2%1)



def solution(input_numbers):
    my_list = list(input_numbers)
    max_num = max(my_list)
    print(max_num)
    prime_list = []
    for i in range(2, max_num):
        is_prime = True
        for x in range(2, i):
            if i % x == 0:
                is_prime = False
        if is_prime == True:
            prime_list.append(i)
    for i in my_list:
        if i in prime_list:
            prime_list.append(i)
    return set(prime_list)

print(solution((2,3,5,35)))
#
#
# for i in range(2, 36):
#     for x in range(2, i)
#         if i


# 两层的loop，第二层才是计算。1不是prime number
# for i in range(2, 101):
#     is_prime = True
#     for x in range(2, i): # 从2开始不被其它数整除，不包括自己
#         if i % x == 0:
#             is_prime = False
#     if is_prime:
#         print(i)


n = 35
def solution(n):
    prime_nums = []
    for num in range(n):
        if num > 1: # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0: # if the modulus == 0 is means that the number can be divided by a number preceding it
                    break
            else:
                prime_nums.append(num)
    return prime_nums
solution(n)


