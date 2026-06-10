class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        L = 0  # slow pointer

        for R in range(1, len(nums)):
            if nums[R] != nums[L]:
                L += 1
                nums[L] = nums[R]  # overwrite the duplicate

        return L + 1  # new length of the unique part
