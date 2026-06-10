class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combos = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in combos:
                combos[key] = []
            combos[key].append(s)
        
        return list(combos.values())