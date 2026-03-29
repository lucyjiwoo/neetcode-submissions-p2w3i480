class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        for val in nums:
            heapq.heappush(self.pq, val)
            if len(self.pq) > k:
                heapq.heappop(self.pq)
        self.kth = self.pq[0] if self.pq else None
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        self.kth = self.pq[0] if self.pq else None
        return self.kth



