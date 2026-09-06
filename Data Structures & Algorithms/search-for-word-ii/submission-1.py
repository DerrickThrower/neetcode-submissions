class TrieNode:
    def __init__(self,val=0):
        self.val = val
        self.next = {}
        self.end = False
        self.word = None


class Solution:
    def __init__(self):
        self.res = []
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        row = len(board)
        col = len(board[0])
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.next:
                    curN = TrieNode(char)
                    cur.next[char] = curN
                cur = cur.next[char]

            cur.end = True
            cur.word = word


        def dfs(r,c,curN):

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "#" or board[r][c] not in curN.next:
                return False

            
            nxt = curN.next[board[r][c]]
            if nxt.end:
                self.res.append(nxt.word)

            originalC = board[r][c]
            board[r][c] = "#"


            #search
            dfs(r+1,c,nxt)
            dfs(r-1,c,nxt)
            dfs(r,c+1,nxt)
            dfs(r,c-1,nxt)


            board[r][c] = originalC



        
        for r in range(row):
            for c in range(col):

                dfs(r,c,root)

        result = list(set(self.res))
        return result
