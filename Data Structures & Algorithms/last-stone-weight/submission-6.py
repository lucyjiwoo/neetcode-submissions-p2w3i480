class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if stones else 0
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
            
        while len(pq)> 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -abs(x-y))
        return -pq[0] if pq else 0
            
