'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''


from typing import List

def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
        return binary_search_recursive(nums, target, left, right)
    else:
        right = mid - 1
        return binary_search_recursive(nums, target, left, right)


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        return binary_search_recursive(nums, target, left=0, right=len(nums) -1)

print(Solution.search(nums=[-1,0,3,5,9,12], target = 9))