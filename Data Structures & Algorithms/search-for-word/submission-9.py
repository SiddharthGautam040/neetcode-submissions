class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i):
            if i >= len(word):
                return True
            
            if r < 0 or r >= len(board):
                return False

            if c < 0 or c >= len(board[0]):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            temp = board[r][c] 
            board[r][c] = '#'

            found = (dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1) or dfs(r-1, c, i+1))
            board[r][c] = temp
            return found

        for ri in range(len(board)):
            for ci in range(len(board[0])):
                if dfs(ri, ci, 0):
                    return True 
        
        return False
                