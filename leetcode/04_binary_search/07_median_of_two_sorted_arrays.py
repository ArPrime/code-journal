'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


from typing import List
class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            cut_1 = (left + right) // 2
            cut_2 = (m + n + 1) // 2 - cut_1
            nums1_left_max = nums1[cut_1 - 1] if cut_1 > 0 else float('-inf')
            nums1_right_min = nums1[cut_1] if cut_1 < m else float('inf')
            nums2_left_max = nums2[cut_2 - 1] if cut_2 > 0 else float('-inf')
            nums2_right_min = nums2[cut_2] if cut_2 < n else float('inf')

            if nums1_left_max <= nums2_right_min and nums1_right_min >= nums2_left_max:
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                else:
                    return max(nums1_left_max, nums2_left_max)
            elif nums1_left_max > nums2_right_min:
                right = cut_1 - 1
            else:
                left = cut_1 + 1

print(Solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))