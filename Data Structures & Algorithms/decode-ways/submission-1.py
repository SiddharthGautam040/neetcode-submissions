class Solution:
    def numDecodings(self, s: str) -> int:
        dp0, dp2 = 0, 0
        dp1 = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp0 = 0
            else:
                dp0 = dp1

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp0 += dp2

            dp0, dp1, dp2 = 0, dp0, dp1
            
        return dp1
