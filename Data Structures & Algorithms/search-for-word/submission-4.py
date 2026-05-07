class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, word, i, j, 0):
                    return True
        return False
        

    def backtrack(self, board, word, br, bc, wp):
        if wp >= len(word):
            return True
        
        if br >= len(board) or bc >= len(board[0]) or bc < 0 or br < 0:
            return False
        
        if board[br][bc] == word[wp]:
            temp = board[br][bc]
            board[br][bc] = "#"
            a = self.backtrack(board, word, br + 1, bc, wp + 1)
            b = self.backtrack(board, word, br, bc + 1, wp + 1)
            c = self.backtrack(board, word, br, bc - 1, wp + 1)
            d = self.backtrack(board, word, br - 1, bc, wp + 1)
            board[br][bc] = temp
            return a or b or c or d
