# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: TreeNode, values: List[int]):
            if not root:
                return
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)
        values = []
        inorder(root, values)
        return values[k - 1]
    



# root = [5,3,6,2,4,null,null,1]
# Space Complexity: O(h)

# h is the height of the tree.

# This is due to the call stack used in recursion.

# In your example, the tree is skewed on the left (deep on one side), so height h = 4.
# in this at a time, only one recursion is active and needs space, so the space used is O(h).