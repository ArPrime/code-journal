'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''


# # Geometric Visualization of the Two Pointer Algorithm for Container With Most Water

# ## Core Insight

# The two-pointer algorithm can be elegantly visualized by mapping the **search space** onto a 2D coordinate system:
# - x-axis represents the left pointer position `i`
# - y-axis represents the right pointer position `j`
# - Each point `(i, j)` represents a possible container configuration

# ## Geometric Representation of the Search Space

# **1. Valid Search Region**
# - All valid `(i, j)` combinations must satisfy `i < j`
# - This forms an upper triangular region bounded by the line `y = x`
# - The total search space is this upper triangle

# **2. Algorithm Trajectory**
# - Starting point: `(0, n-1)` - upper left corner
# - Movement rules: can only move right (`i++`) or down (`j--`)
# - End point: somewhere near the diagonal, like `(n-2, n-1)`

# **3. Dynamic Search Space Reduction**
# When the pointers are at position `(i, j)`, the remaining search space forms a triangle bounded by three lines:
# - Vertical line `x = i` (left boundary of searched region)
# - Horizontal line `y = j` (upper boundary of searched region)  
# - Diagonal line `y = x` (natural boundary of the lower triangle)

# ## Why This Visualization Matters

# This geometric perspective clearly illustrates why the two-pointer algorithm doesn't miss the optimal solution - the "pruned" regions (areas proven to not contain better solutions) are geometrically well-defined and systematically eliminated.

# The algorithm essentially performs a smart traversal from the upper-left corner toward the diagonal, shrinking the remaining search triangle at each step while guaranteeing that no better solution exists in the eliminated areas.


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        
        while i < j:
            current_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, current_area)

            if height[i] < height[j]:
                i +=1
                while i < j and height[i-1] > height[i]:
                    i += 1
            else:
                j -= 1
                while i < j and height[j+1] > height[j]:
                    j -= 1
        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))