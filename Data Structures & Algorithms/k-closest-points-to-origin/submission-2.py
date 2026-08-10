import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []
        heapq.heapify(h)

        for p in points:
            x1, y1 = p[0], p[1]

            dis = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)

            heapq.heappush(h,(-dis,p))

            if len(h) > k:
                heapq.heappop(h)
                

        res = []
        for i in h:
            res.append(i[1])
        return res

