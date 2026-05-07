class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF, res, l = 0, 0, 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxF = max(maxF, freq[s[r]]) 

            while ((r - l + 1) - maxF) > k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
            res = max(res, r - l + 1)
        
        return res
