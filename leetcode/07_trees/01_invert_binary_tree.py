'''
Given the root of a binary tree, invert the tree, and return its root.

The number of nodes in the tree is in the range [0, 100].


Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
'''


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root