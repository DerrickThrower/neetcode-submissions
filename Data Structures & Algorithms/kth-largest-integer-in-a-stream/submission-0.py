import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = [s for s in nums]
        heapq.heapify(self.h)

        while len(self.h) > k:
            heapq.heappop(self.h)
        

        self.k = k

    def add(self, val: int) -> int:

        heapq.heappush(self.h,val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]

    
        
