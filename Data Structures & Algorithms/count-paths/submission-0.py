class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)]for j in range(m)]
        
        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if i + 1 >= n or j + 1 >= m:
                    dp[j][i] = 1
                else:
                    dp[j][i] = dp[j+1][i] + dp[j][i+1]
        return dp[0][0]