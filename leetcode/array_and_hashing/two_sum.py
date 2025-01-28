from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target - num], i]
            my_dict[num] = i