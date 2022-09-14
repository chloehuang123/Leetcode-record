class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
      
 ###############################################################################################
# set这个函数主要是用在not in/in里面查找，原理是用for和while loop找到consecutive的头
###############################################################################################
