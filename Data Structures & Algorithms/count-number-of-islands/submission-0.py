from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count+=1
                    queue = deque([(r,c)])

                    while queue:
                        r2, c2 = queue.popleft()
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = r2 + dr, c2 + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"   # mark on push
                                queue.append((nr, nc))



        return count