class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        
        l = 0
        window = {}
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            
            if window == freq:
                return True
        
        return False
            
