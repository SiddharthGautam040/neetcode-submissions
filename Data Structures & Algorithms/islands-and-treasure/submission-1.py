class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs():
            
            while q:
                row, col, lvl = q.popleft()

                paths = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]
                for r, c in paths:
                    if 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]):
                        if grid[r][c] == 2147483647:
                            grid[r][c] = min(lvl+1, grid[r][c]) 
                            q.append((r,c,lvl+1))

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        bfs()
        return None