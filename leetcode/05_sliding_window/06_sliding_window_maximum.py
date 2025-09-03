'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Constraints:

1 <= nums.length <= 10^5
1 <= k <= nums.length

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''


from collections import deque
from typing import List

class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        dq = deque()
        dq.append(0)
        result = []

        for i, num in enumerate(nums):
            if dq[0] <= i - k:
                dq.popleft()
            while dq and num >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i > k - 2:
                result.append(nums[dq[0]])
        
        return result


print(Solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))