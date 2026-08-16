class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        rows, cols = len(grid),len(grid[0])


        def dfs(r,c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
                
            if not grid[r][c] or grid[r][c] == "0":
                return 0

            
            grid[r][c] = "0"


            return 1 + dfs(r,c+1) + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1)


        for i in range(rows):
            for j in range(cols):

                cur = dfs(i,j)

                maxA = max(maxA,cur)


        return maxA

