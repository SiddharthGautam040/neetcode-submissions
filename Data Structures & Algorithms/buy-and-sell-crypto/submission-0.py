class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        min_buy = prices[0]
        profit = 0

        while r < n:
            min_buy = min(prices[l], min_buy)
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
                profit = max(prices[r] - min_buy, profit)
            l += 1
            r += 1
        return profit
           