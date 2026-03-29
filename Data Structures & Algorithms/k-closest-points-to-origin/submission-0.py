class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            d_sqr = point[0]**2 + point[1]**2
            heapq.heappush(pq, ([-d_sqr,point]))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        for p in pq:
            res.append(p[1])
        return res
