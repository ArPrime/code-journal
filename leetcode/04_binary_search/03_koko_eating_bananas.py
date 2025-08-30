'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
'''


from typing import List

class Solution:
    @staticmethod
    def minEatingSpeed(piles: List[int], h: int) -> int:
        def can_fishish(speed) -> bool:
            total_time = 0
            for pile in piles:
                total_time += (pile + speed - 1) // speed
            return total_time <= h
        
        right = max(piles)
        left = (sum(piles) + h - 1) // h

        while left < right:
            mid = (left + right) // 2
            if can_fishish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

print(Solution.minEatingSpeed(piles = [3,6,7,11], h = 8))     