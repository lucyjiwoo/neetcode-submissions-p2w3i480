class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        for n in nums:
            if len(self.data)<k:
                heapq.heappush( self.data, n)
            else:
                if self.data[0] < n:
                    heapq.heappop( self.data)
                    heapq.heappush( self.data,n)

    def add(self, val: int) -> int:
        if len(self.data)<self.k:
                heapq.heappush(self.data, val)
        else:
            if self.data[0] < val:
                heapq.heappop(self.data)
                heapq.heappush(self.data,val)
        return self.data[0]