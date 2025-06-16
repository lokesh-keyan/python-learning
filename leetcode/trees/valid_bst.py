# Definition for a binary tree node
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(root: TreeNode) -> bool:
            nonlocal prev
            if not root:
                return True
            
            if not (inorder(root.left) and prev < root.val):
                return False
            prev = root.val
            return inorder(root.right)
        return inorder(root)