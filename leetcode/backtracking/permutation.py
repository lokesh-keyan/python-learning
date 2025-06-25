from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack()
                    curr.pop()
            
        res = []
        curr = []
        backtrack()
        return res
    

# O(n! × n) total, plus O(n) auxiliary space for recursion and temp state.

# Final Time Complexity:
# O(n! × n)

# n! permutations

# O(n) work to check/set up each one (mainly due to num not in curr)