class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        index = 0
        ROWS, COLS = len(board), len(board[0])
        def search(r,c,index):
            if index == len(word):
                return True


            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            if board[r][c] == "#":
                return False

            if board[r][c] != word[index]:
                return False


            board[r][c] = "#"


            res = (search(r+1,c,index+1) 
            or search(r-1,c,index+1)
            or search(r,c+1,index+1)
            or search(r,c-1,index+1))
            board[r][c] = word[index]

            return res


        for r in range(ROWS):
            for c in range(COLS):
                if search(r, c, 0):
                    return True
        return False
        



    
        


        