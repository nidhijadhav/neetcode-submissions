class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)

        window = {}
        have, need = 0, len(freqT)
        res = ""
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in freqT and window[c] == freqT[c]:
                have += 1

            while have == need:
                # Update result
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                # Shrink window
                window[s[l]] -= 1
                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        
        return res