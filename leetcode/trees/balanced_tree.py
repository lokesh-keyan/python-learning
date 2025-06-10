# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if not root:
                return True, 0
            
            left_balanced, left_height = depth(root.left)
            right_balanced, right_height = depth(root.right)

            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return is_balanced, 1 + max(left_height, right_height)

        is_balanced, height = depth(root)
        return is_balanced