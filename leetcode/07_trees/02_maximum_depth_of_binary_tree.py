'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
    


# Alternative iterative solution using BFS (level-order traversal)
from collections import deque

class SolutionIterative:
    def maxDepth(self, root):
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return max_depth