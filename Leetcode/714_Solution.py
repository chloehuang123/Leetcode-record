class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sold = 0

        for i in range(1, len(prices)):
            buy = max(buy, sold - prices[i])
            sold = max(sold, buy+prices[i] - fee)
        return sold
