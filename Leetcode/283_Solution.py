"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
