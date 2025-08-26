# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]


from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_to_frequency = {}
        for num in nums:
            element_to_frequency[num] = element_to_frequency.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for element, frequency in element_to_frequency.items():
            bucket[frequency].append(element)
        
        top_k_element = []
        for i in range(len(nums), 0, -1):
            for element in bucket[i]:
                top_k_element.append(element)
            if len(top_k_element) == k:
                return top_k_element


sol = Solution()
test_nums = [1, 2, 2, 3, 3]
print(sol.topKFrequent(test_nums, 2))