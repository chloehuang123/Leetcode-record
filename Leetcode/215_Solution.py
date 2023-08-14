"""
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = self.merge_sort(nums)
        return sorted_nums[-k]

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
        


    def merge(self,left, right):
        low, high = 0,0
        res = []

        while low < len(left) and high < len(right):
            if left[low] < right[high]:
                res.append(left[low])
                low += 1
            else:
                res.append(right[high])
                high += 1
            
        res.extend( left[low:] )
        res.extend( right[high:] )
        return res
