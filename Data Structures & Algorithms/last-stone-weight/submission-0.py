import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)


        while len(h) > 1:

            y = heapq.heappop(h)
            x = heapq.heappop(h)

            if -(x) < -(y):
                y = -(x) - -(y)
                heapq.heappush(h, y)

            else:
                pass


        return -(heapq.heappop(h)) if len(h)>0  else 0  
     