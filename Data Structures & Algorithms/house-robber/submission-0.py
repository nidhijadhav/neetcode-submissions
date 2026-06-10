class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        
        twoAway = nums[0]
        oneAway = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            currHouse = max(oneAway, twoAway + nums[i])
            twoAway = oneAway
            oneAway = currHouse
        
        return oneAway