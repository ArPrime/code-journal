'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num-1 in nums_set:
                continue
            length = 1
            while num+1 in nums_set:
                length += 1
                num += 1
            
            longest = max(length, longest)

        return longest

sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))