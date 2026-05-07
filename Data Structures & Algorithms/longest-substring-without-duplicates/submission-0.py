class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l = 0

        for i in range(len(s)):
            if s[i] in mp:
                l = max(l, mp[s[i]] + 1)
            mp[s[i]] = i
            res = max(res, i - l + 1)
        return res