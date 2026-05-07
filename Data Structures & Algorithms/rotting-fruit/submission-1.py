from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        mins = 0
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                nei = [[0,1],[1,0],[-1,0],[0,-1]]

                for sr, sc in nei:
                    nr = sr + r
                    nc = sc + c
                    if 0 <= nc < len(grid[0]) and 0 <= nr < len(grid) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            
            mins += 1
        return mins if fresh == 0 else -1


