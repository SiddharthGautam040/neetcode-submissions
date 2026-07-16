class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        seen = {}
        while r < len(s):
            if s[r] in seen:
                ri = seen[s[r]]
                while l <= ri:
                    del seen[s[l]]
                    l = l + 1
            res = max(r-l+1, res)
            seen[s[r]] = r
            r = r + 1
        return res