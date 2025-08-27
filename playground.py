class Solution:
    def threeSum(self, nums: list):
        res = []
        nums.sort()

        i = 0  # Initialize the index
        while i < len(nums):  # Set the loop condition
            if i > 0 and nums[i] == nums[i-1]:
                i += 1  # Manually increment
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
            
            i += 1  # Manually increment the outer loop index

        return res
    
sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))