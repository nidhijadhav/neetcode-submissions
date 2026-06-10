class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1  # min must be to the right
            else:
                r = m  # min could be at m or to the left

        return nums[l]