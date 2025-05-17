class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                
                while n + length in num_set:
                    length += 1
                
                longest_sequence = max(longest_sequence, length)        
        
        return longest_sequence