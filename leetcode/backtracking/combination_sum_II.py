from typing import List


class Solution:
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()
        
        backtrack(0, target)
        return res