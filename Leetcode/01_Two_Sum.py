class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTb = {}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in hashTb:
                return [hashTb[target - num], i]
            hashTb[num] = i

            
            
            

###############################################################################################
# 最后不能用 如[Valid_Anagram](https://github.com/chloehuang123/Leetcode-record/blob/main/Leetcode/242_Valid_Anagram.py)
###############################################################################################
