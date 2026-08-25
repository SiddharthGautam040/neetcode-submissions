class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r, c, q):
            if r >= n or c < 0 or c >= n:
                return

            if self.isValid(r, c, n, board):
                board[r][c] = "Q"

                if q + 1 == n:
                    res.append(["".join(row) for row in board])
                else:
                    for col in range(n):
                        dfs(r + 1, col, q + 1)

                # Backtrack
                board[r][c] = "."

        for c in range(n):
            dfs(0, c, 0)

        return res

    def isValid(self, r, c, n, board):
        # Check same column above
        i = r - 1
        while i >= 0:
            if board[i][c] == "Q":
                return False
            i -= 1

        # Check upper-left diagonal
        i, j = r - 1, c - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = r - 1, c + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True