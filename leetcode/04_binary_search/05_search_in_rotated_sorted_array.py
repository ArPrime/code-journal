'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

All values of nums are unique.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


# def search_coordinate_mapping(nums, target):
#     """
#     使用坐标映射的方法：
#     1. 找到旋转点
#     2. 通过坐标映射在逻辑上"还原"数组，直接在原数组上操作
#     3. 如果计算出的索引超过数组长度，就减去数组长度
#     """
#     if not nums:
#         return -1
    
#     n = len(nums)
    
#     # 步骤1: 找到最小值的位置（旋转点）
#     def find_minimum_index():
#         left, right = 0, n - 1
        
#         # 如果数组没有被旋转
#         if nums[left] <= nums[right]:
#             return 0
        
#         while left < right:
#             mid = (left + right) // 2
            
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
        
#         return left
    
#     # 找到旋转点
#     rotation_index = find_minimum_index()
    
#     # 步骤2: 使用坐标映射进行二分查找
#     left, right = 0, n - 1
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         # 关键：坐标映射
#         # 将逻辑上的 mid 映射到实际数组的索引
#         real_mid = (mid + rotation_index) % n
        
#         if nums[real_mid] == target:
#             return real_mid
#         elif nums[real_mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return -1

# print(search_coordinate_mapping(nums = [4,5,6,7,0,1,2], target = 0))
# print(search_coordinate_mapping(nums = [4,5,6,7,0,1,2], target = 3))


from typing import List

class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if  nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

print(Solution.search(nums = [4,5,6,7,0,1,2], target = 0))
print(Solution.search(nums = [4,5,6,7,0,1,2], target = 3))