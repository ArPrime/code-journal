from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            else:
                num_to_index[num] = i

sol = Solution()
nums_1 = [1, 2, 3, 4]
target_1 = 5
print(sol.twoSum(nums_1, target_1))