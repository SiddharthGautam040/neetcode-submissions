class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        ct, window = {}, {}
        for i in t:
            ct[i] = 1 + ct.get(i, 0)

        l = 0
        need = len(ct)
        have = 0
        res, resLen = [-1, -1], float("infinity")
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            
            if s[r] in ct and window[s[r]] == ct[s[r]]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in ct and window[s[l]] < ct[s[l]]:
                    have -= 1
                l = l + 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
                