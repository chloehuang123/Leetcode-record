class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        def merge(left, right):
            low, high = 0, 0
            res = []

            while low < len(left) and high < len(right):
                if left[low] > right[high]:
                    res.append(right[high])
                    high += 1
                else:
                    res.append(left[low])
                    low += 1
            
            while low < len(left):
                res.append(left[low])
                low += 1

            while high < len(right):
                res.append(right[high])
                high += 1
            return res

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return merge(left, right)
            
