class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, curr_sum):
            if curr_sum > amount:
                return 0
            if i >= len(coins):
                return 1 if curr_sum == amount else 0
            if curr_sum == amount:
                return 1
            if (i, curr_sum) in dp:
                return dp[(i,curr_sum)] 
            
            
            dp[(i, curr_sum)] = dfs(i+1, curr_sum) + dfs(i, curr_sum + coins[i])

            return dp[(i,curr_sum)]

        return dfs(0, 0)
