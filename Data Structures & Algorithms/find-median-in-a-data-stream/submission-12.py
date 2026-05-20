class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        
        if self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

        
    def findMedian(self) -> float:
        if not self.left and not self.right:
            return 0.0
        if len(self.left) == len(self.right):
            n1 = -self.left[0]
            n2 = self.right[0]
            return (n1+n2)/2
        else:
            return -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        