class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.helper(i, i, s)
            res += self.helper(i, i+1, s)
        return res
            

    def helper(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l = l - 1
            r = r + 1
        return res
