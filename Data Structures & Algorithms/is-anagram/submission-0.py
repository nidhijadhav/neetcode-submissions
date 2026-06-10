class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}

        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c in t:
            seen[c] = seen.get(c, 0) - 1
            if seen[c] == 0:
                seen.pop(c)
        
        return not seen