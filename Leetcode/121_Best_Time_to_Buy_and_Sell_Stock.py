class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

###############################################################################################
# 思路：找到最小，然后往后找
###############################################################################################
