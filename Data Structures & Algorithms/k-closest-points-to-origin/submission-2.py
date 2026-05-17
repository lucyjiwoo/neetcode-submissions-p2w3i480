class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClosest = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            heapq.heappush(kClosest,(-dist,p))
            while len(kClosest)> k:
                heapq.heappop(kClosest)

        return [d[1] for d in kClosest]