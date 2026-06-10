class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, n in enumerate(nums):
            if n in pairs:
                return [pairs[n], i]
            pairs[target - n] = i
        