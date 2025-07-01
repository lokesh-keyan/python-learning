from collections import Counter
from typing import List

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # converts into freq, actualValue dict

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num) #list of list, multiple values can have same freq, so freq is the index of the list inside bucket
        
        result = []
        for i in range(len(nums), 0, -1): # this goes in reverse order, so we get the most frequent first
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result