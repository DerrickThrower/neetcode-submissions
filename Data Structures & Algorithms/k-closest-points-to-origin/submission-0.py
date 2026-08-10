import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []
        heapq.heapify(h)

        for p in points:
            x1, y1 = p[0], p[1]

            dis = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)

            heapq.heappush(h,(dis,p))


        count = 0
        res = []
        while count < k:

            val = heapq.heappop(h)

            res.append(val[1])  
            count += 1 

        return res

