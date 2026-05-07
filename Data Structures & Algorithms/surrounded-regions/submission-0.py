class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return 
            
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r - 1 < 0 or r + 1 == ROWS) or (c-1 < 0 or c+1 == COLS) and board[r][c] == "O":
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        