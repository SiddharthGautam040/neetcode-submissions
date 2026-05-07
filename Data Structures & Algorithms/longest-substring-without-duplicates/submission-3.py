class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] in mp:
                l = max(mp[s[i]] + 1, l)
            res = max(r - l + 1, res)
            mp[s[i]] = i
            r = i + 1
        return res