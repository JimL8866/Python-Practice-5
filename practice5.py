# import collections
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         c = collections.Counter(nums)
#         is_duplicate = False
#         for i in c.values():
#             if i > 1:
#                 is_duplicate = True
#                 break
#         return is_duplicate
#
# s = Solution()
# print(s.containsDuplicate([2,14,18,22,22]))


import collections
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         my_set = set(nums)
#         if len(my_set) != len(nums):
#             return True
#         else:
#             return False
#
# s = Solution()
# print(s.containsDuplicate([2,14,18,22,22]))

# class Solution(object):
#     def maxSubArray(self, nums):
#         res = nums[0]
#         pre = 0
#         for i in range(len(nums)):
#             pre = max(nums[i],pre+nums[i])
#             res = max(res, pre)
#         return res

# def rotate(my_list, num_rotations):
#   for i in range(num_rotations):
#     my_list.insert(0, my_list.pop())
#     return my_list
#
# print(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2))

# import collections
# def remove_duplicates(dupe_list):
#   c = collections.Counter(dupe_list)
#   return c.keys()
#
# print(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']))


# def findMedianSortedArrays(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: float
#     """
#     nums1.extend(nums2)
#     nums1.sort()
#     print(nums1)
#     size = len(nums1)
#     if size % 2 == 1:
#         return nums1[(size-1)//2]
#     elif len(nums1) % 2 == 0:
#         return (nums1[size//2] + nums1[size//2-1])/2
#
# print(findMedianSortedArrays([1,2], [3,4]))

mapping = {"age" : 16, "name": "jim" }
del mapping["age"]
print(mapping)