class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26

        l1 = len(s1)
        l2 = len(s2)
        l, r = 0, 0

        for i in s1:
            c1[ord(i) - ord('a')] += 1
        
        while r < l2:
            if r >= l1:
                c2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            c2[ord(s2[r]) - ord('a')] += 1
            if c1 == c2:
                return True

            r += 1
        return False
