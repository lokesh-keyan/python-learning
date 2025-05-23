from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        i = 0
        result = 0

        for j in range(len(s)):
            freq[s[j]] += 1
            maxFreq = max(freq.values())
            currLen = j - i + 1
            if currLen - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        
        return result