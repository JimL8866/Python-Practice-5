# import collections
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     max_num = 0
#     sub = collections.deque()
#     for i in range(len(s)):
#         if s[i] not in sub:
#             sub.append(s[i])
#             if max_num < len(sub):
#                 max_num = len(sub)
#         else:
#             while s[i] in sub:
#                 sub.popleft()
#             sub.append(s[i])
#             print(sub)
#     return max_num
#
# print(lengthOfLongestSubstring("abcdabcd"))

#
# strs = ["flower","flow","flight"]
# new_str = sorted(strs, key=len)
# print(new_str)
# print(strs)
#
# char = min(strs, key=len)
# char2 = max(strs, key=len)
# print(char)
# print(char2)
#
#
# def findMaxConsecutiveOnes(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if not nums:
#         return 0
#     res, counter = 0, 0
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             counter += 1
#             if res < counter:
#                 res = counter
#         else:
#             counter = 0
#     return res
#
#
# nums = None
# print(findMaxConsecutiveOnes(nums))
# my_list = []
# my_dict = {"jim":35, "julie": 34, "lixa": 60}
# for k, v in my_dict.items():
#     my_list.append([k,v])
# print(my_list)
# my_tuple = tuple(my_list)
# print(my_tuple)
#
# my_list=["a", "b", "c", "d", "e"]
# set = set(my_list)
# print(set)
# for i in set:
#     print(i)
#
# a = "a1234a"
# b = a.strip("a")
# print(b)

# a = "hello"
# b = a.upper()
# print(a)
# print(b)

# thislist = ["apple", "banana", "banana","cherry"]
# # for i in thislist:
# #     if i == "banana":
# #         thislist.remove("banana")
# #         print(thislist)
#
# new_list = []
# for i in thislist:
#     if i != "banana":
#         new_list.append(i)
# print(new_list)
# m = "abc"
# n = "abc"
# str= []
# for i in range(len(m)):
#     z = m[i]+n[i]
#     str.append(z)
#
# new_str ="".join(str)
# print(new_str)

# questions = ['name', 'colour', 'shape']
#
# answers = ['apple', 'red', 'a circle']
#
# new_list = []
#
# obj = zip(questions, answers)
# for i,j in obj:
#     new_list.append([i,j])
#
#
# print(new_list)

# my_list = [['name', 'apple'], ['colour', 'red']]
# i, j = my_list
# print(i)
# print(j)

# my_list_2 = [['name', 'apple'], ['colour', 'red'], ['shape', 'a circle']]
# i, j = zip(*my_list_2)
# print(i)
# print(j)

# a = "hello"
# b = reversed(a)
# for i in reversed(range(1,10)):
#     print(i)


# questions = ['name', 'colour', 'shape']
#
# answers = ['apple', 'red', 'a circle']
#
# for i in range(len(questions)):
#     questions.insert(i, answers[i])
#
# print(questions)

# user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
#
# for i in range(len(user_list)):
#     while "Alex" in user_list:
#         user_list.remove("Alex")
#
# print(user_list)
#
# # a = "How are you, jim"
# #
# # idx = a.find("are")
# # print(idx)
# # length = len("are")
# # b = a[0:idx] + a[idx+length+1:]
# # print(b)
#
# # questions = ['name', 'colour', 'shape']
# # questions[-1:1]= [23]
# #
# # print(questions)
# a = 12345
# b = list(a)
# print(b)

# tuple1 = (1, 2, 3, 4, 5)
# new_tup = tuple1 * 2
# print(new_tup)
# print(tuple1[::-1])

# a = "hello"
# print(tuple(a))
# list1 = [1, 2, 3, 4, 5]
# list2 = list1[2:5]
# print(list1)
# print(list2)

# s1 = {"刘能", "赵四", "⽪⻓⼭"}
# s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
#
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.union(s2))
#
# s1.symmetric_difference(s2)
#
# s1 = {"刘能", "赵四", "⽪⻓⼭"}
# s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# s3 = s1 & s2
# print(s3)
#
# s1 = {"刘能", "赵四", "⽪⻓⼭"}
# s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# s3 = s1 | s2
# print(s3)


# s1 = {"刘能", "赵四", "⽪⻓⼭"}
# s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
#
# v = True if "刘能" in s1 else False
#
# print(v)

# info = {"age":12, "status":True, "name":"wupeiqi","email":"xx@live.com"}
# data = info.keys()
#
# print(list(data))

# questions = ['name', 'colour', 'shape']
# del questions[:]
# print(questions)
#
# info = {"age":12, "status":True, "name":"wupeiqi","email":"xx@live.com"}
#
# del info["age"]
#
# print(info)


# old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}
#
# new_price = {k: v for k, v in old_price.items() if v >=2.5}
# print(new_price)


# my_list = [['name', 'apple'], ['colour', 'red']]
# my_dict = dict(my_list)
# print(my_dict)
# new_list = []
# for i in my_list:
#     new_list.append(tuple(i))
#
# print(new_list)
#
# new_dict = dict(new_list)
# print(new_dict)

# info = {"age":12, "status":True, "name":"wupeiqi","email":"xx@live.com"}
#
# my_list = [[i, v] for i, v in info.items()]
# print(my_list)

# stats = {'z': 1000, 'x': 3000, 'j': 100}
# max_value2 = max(stats)
# print(max_value2)
#
# max_value = max(stats, key=stats.get)
# print(max_value)
# print(stats[max_value])

# lst1=[2, 4, 6, 8, 10, 12, 14]
#
# #Type your answer here.
#
# lst2=[i**2 if i**2 > 50 else  for i in lst1]
#
#
# # print(lst2)
# import collections
# def solution(s):
#     c = collections.Counter(s)
#     print(c)  #Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
#     my_dict = dict(c)
#     print(my_dict)   #{'H': 1, 'e': 1, 'l': 2, 'o': 1}
#     my_list = list(c)
#     print(my_list)  #['H', 'e', 'l', 'o']
#     my_e = list(c.elements())
#     print(my_e)  #['H', 'e', 'l', 'l', 'o']  #按照元素出现次数迭代。
#     print(sorted(c))   #['H', 'e', 'l', 'o']
#     print(c.items())   #dict_items([('H', 1), ('e', 1), ('l', 2), ('o', 1)])
#     # for k, v in c.items()  #自带的items() 方法
#     print(c.most_common(1))  #[('l', 2)] 出现次数最多的一个元素
#     print(c.most_common())  #[('l', 2), ('H', 1), ('e', 1), ('o', 1)] 没有指定就全部出现
# print(solution("Hello"))
#
# c = collections.Counter([1,9,9,5,0,8,0,9])
# print(c)   #counter obj 不是按照顺序
# print(dict(c))   # dict 是按照顺序的
#


# list_01 = [1,9,9,5,0,8,0,9]
# c = collections.Counter(list_01)
# print(c)

#
# def is_prime(num):
#     if num == 1:
#         return "it is not a prime number"
#     else:
#         prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 prime = False
#         if prime:
#             return "it is a prime number"
#         else:
#             return "not a prime number"
#
# print(is_prime(22))
#
# def solution(num):
#     if num <= 1:
#         return "no prime numbers"
#     else:
#         prime_list = []
#         prime = True
#         for i in range(2, num):
#             for j in range(2, i):
#                 if i % j == 0:
#                     prime = False
#                     break
#                 else:
#                     prime = True
#             if prime == True:
#                 prime_list.append(i)
#         return prime_list
#
# print(solution(35))

list1 = [10, 20, 4, 45, 99]
list2 = map(lambda x : x*3, list1)
print(sum(list(list2)))