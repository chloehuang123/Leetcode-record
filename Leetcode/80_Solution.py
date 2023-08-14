"""
each unique element appears at most twice
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2

        while i < len(nums):

            if nums[i] == nums[i - 2]:
                nums.pop(i)
            else: 
                i += 1
