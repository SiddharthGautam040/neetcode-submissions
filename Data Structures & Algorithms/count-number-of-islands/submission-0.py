class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        rl, cl = len(grid), len(grid[0])

        def dfs(r, c):
            self.res += 1
            q = [(r, c)]
            while q:
                cr, cc = q.pop(0)
                grid[cr][cc] = "#"
                for rs, cs in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                    if -1 < rs < rl and -1 < cs < cl and grid[rs][cs] == "1":
                        q.append((rs, cs))

        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == "1":
                    dfs(r, c)
        return self.res