class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        rest = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        rest[0] = 0
        sell[0] = 0

        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            rest[i] = max(rest[i-1], buy[i-1], sell[i-1])
            buy[i] = max(buy[i-1], rest[i-1] - prices[i])

        return sell[len(prices) - 1]
