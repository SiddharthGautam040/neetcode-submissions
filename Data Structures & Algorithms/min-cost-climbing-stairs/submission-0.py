class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        dp = [0 for i in range(len(cost))]

        for i in range(len(cost) - 1, -1, -1):
            if i + 2 >= len(cost):
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])