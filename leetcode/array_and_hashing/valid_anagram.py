class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = {}
        for ch in s:
            result[ch] = result.get(ch, 0) + 1
        
        for ch in t:
            if ch not in result or result[ch] == 0:
                return False
            result[ch] -= 1
        
        return True