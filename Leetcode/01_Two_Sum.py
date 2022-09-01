class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTb = {}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in hashTb:
                return [hashTb[target - num], i]
            hashTb[num] = i

            
            
            

###############################################################################################
# 最后不能用 如Valid_Anagram中 hashTb.get( , ), 因为第二个input必须是个value
# https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
###############################################################################################

