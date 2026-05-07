class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack(n, 0, 0, "", 0)
        return self.res

    def backtrack(self, n, o, c, curr,l):
        if l > (2*n):
            return
        
        if l == (2 * n) and o == n and c == n:
            self.res.append(curr[:])
            return
        
        if o < n:
            self.backtrack(n, o + 1, c, curr + '(', l + 1)
    
        if c < o:
            self.backtrack(n, o, c + 1, curr + ')', l + 1)

        return