class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)

        if len(nums) > len(distinct):
            return True

        return False