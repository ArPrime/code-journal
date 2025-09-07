'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

nums.length == n + 1
1 <= nums[i] <= n
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''


from typing import List

class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
print(Solution.findDuplicate([1,3,4,2,2]))