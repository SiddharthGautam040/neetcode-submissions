class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0

        for price in prices:
            profit = max(price - min_buy, profit)
            min_buy = min(min_buy, price)
        return profit
            