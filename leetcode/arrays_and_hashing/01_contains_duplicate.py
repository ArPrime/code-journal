from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

sol = Solution()
my_list = [1, 2, 3, 4, 1]
print(sol.containsDuplicate(my_list))