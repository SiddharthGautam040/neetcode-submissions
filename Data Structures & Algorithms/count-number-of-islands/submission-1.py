class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        res = 0
        def dfs(r, c):
            if (r,c) in visited:
                return 
            visited[(r,c)] = True
            paths = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

            for row, col in paths:
                if row < 0 or row >= len(grid):
                    continue
                if col < 0 or col >= len(grid[0]):
                    continue
                if grid[row][col] == "1":
                    dfs(row, col)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    res += 1

        return res
        