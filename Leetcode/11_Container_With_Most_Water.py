class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -=1
        return res


###############################################################################################
# 注意：line 7最后是乘以 r - l 而不是 r - 1
###############################################################################################
