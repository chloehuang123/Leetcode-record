class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        arr = [0] * len(prices)

        for i in range(k):
            buy = -prices[0]
            sell = 0

            for j in range(1, len(prices)):
                buy = max(buy, arr[j] - prices[j])
                sell = max(sell, buy + prices[j])
                arr[j] = sell
        return arr[len(prices) - 1]
