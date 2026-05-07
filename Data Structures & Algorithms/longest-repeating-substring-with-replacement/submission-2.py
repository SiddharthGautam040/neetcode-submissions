class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF, res, i = 0, 0, 0
        freq = {}
        l, r = 0, 0

        while i < len(s):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            maxF = max(maxF, freq[s[i]])
            if ((r - l + 1) - maxF <= k):
                res = max(res, r - l + 1)
                r += 1
            else:
                freq[s[l]] -= 1
                l += 1
                r += 1
            i += 1
        return res