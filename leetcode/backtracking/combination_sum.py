from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def sum_func(sum: int, idx: int):
            if sum == target:
                res.append(sub[:]) # this is to make a copy of the current subset. If i use sub, the sub will be modified in the next recursive call, 
                # so the final result will not be correct.
                return

            if idx >= len(candidates) or sum > target:
                return
            
            sub.append(candidates[idx]) 
            sum_func(sum + candidates[idx], idx)

            sub.pop()
            sum_func(sum, idx + 1)

        sum_func(0, 0)
        return res