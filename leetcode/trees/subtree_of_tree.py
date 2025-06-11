# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_sub_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return is_same_tree(root.left, subRoot.left) and is_same_tree(root.right, subRoot.right)
            
            return False
        
        if not root or not subRoot:
            return False
        
        if is_same_tree(root, subRoot):
            return True

        return self.is_sub_tree(root.left, subRoot) or self.is_sub_tree(root.right, subRoot)