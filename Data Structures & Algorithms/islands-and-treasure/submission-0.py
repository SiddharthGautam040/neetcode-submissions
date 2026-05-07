from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for rn, cn in [[0,1], [1,0], [-1,0], [0,-1]]:
                if 0 <= rn + r < len(grid) and 0 <= cn + c < len(grid[0]) and grid[rn + r][cn + c] == 2147483647:
                    grid[rn + r][cn + c] = grid[r][c] + 1
                    q.append((rn + r, cn + c))
            
            
        

