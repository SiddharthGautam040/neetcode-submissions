class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        area = 0
        def dfs(r,c):
            if (r,c) in visited:
                return 0

            visited[(r,c)] = True
            paths = [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
            curr_area = 1
            for row, col in paths:
                if (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])) and grid[row][col] == 1:
                    curr_area += dfs(row,col)
            return curr_area

                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(dfs(r,c),area)

        return area