class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set()

        for n in nums:
            if n in distinct:
                return True
            distinct.add(n)
        
        return False