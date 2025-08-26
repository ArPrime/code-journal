'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


# # version 1
# # `results[0:0] = [result]` is not efficient

# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left_products = []
#         left_product = 1
#         for num in nums:
#             left_product *= num
#             left_products.append(left_product)
        
#         results = []
#         right_product = 1
#         for i in range(len(nums)-1, 0, -1):
#             result = right_product * left_products[i-1]
#             results[0:0] = [result]
#             right_product *= nums[i]
        
#         results[0:0] = [right_product]
        
#         return results



from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        results = [1] * n
        left_product = 1
        right_product = 1

        for i in range(n):
            results[i] = left_product
            left_product *= nums[i]

        for i in range(n-1 , -1, -1):
            results[i] *= right_product
            right_product *= nums[i]

        return results


sol = Solution()
test_nums = [1, 2, 3, 4]
print(sol.productExceptSelf(test_nums))