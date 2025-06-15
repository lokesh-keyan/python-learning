# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def good_nodes(self, root: TreeNode) -> int:
        def solve(root: TreeNode, val: int) -> int:
            if root:
                k = solve(root.left, max(root.val, val)) + solve(root.right, max(root.val, val))
                if root.val >= val:
                    k += 1
                return k
            return 0
        return solve(root, root.val)