class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        rl, cl = len(grid), len(grid[0])

        def dfs(r, c):
            q = [(r, c)]
            grid[r][c] = "-"
            curr_res = 1
            while q:
                cr, cc = q.pop(0)
                for rs, cs in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                    if -1 < rs < rl and -1 < cs < cl and grid[rs][cs] == 1:
                        grid[rs][cs] = "-"
                        curr_res += 1
                        q.append((rs, cs))
            return curr_res
            
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 1:
                    self.res = max(self.res, dfs(r, c))
        return self.res
