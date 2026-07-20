class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in board:
            rowSet = set()
            for c in r:
                if c !="." and c in rowSet:
                    return False
                rowSet.add(c)

        
        for n in range(9):
            colSet = set()
            for r in range(9):
                if board[r][n] != "." and board[r][n] in colSet:
                    return False
                colSet.add(board[r][n])


        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        


        return True
        