class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, o, c):
            if len(curr) == n * 2:
                if o == c:
                    res.append(curr[:])
                return

            if o < n:
                curr += "("
                dfs(curr, o+1, c)
                curr = curr[:-1]
                        
            if c < n and o > c:
                curr += ")"
                dfs(curr, o, c+1)
                curr = curr[:-1]
            
        dfs("", 0, 0)
        return res
