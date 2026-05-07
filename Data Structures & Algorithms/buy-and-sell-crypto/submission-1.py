class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0

        for i in prices:
            profit = max(i - min_buy, profit)
            min_buy = min(i, min_buy)
        return profit