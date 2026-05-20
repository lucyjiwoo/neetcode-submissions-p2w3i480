class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
        elif len(self.left) == len(self.right):
            if -self.left[0] <= num :
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
        elif len(self.left) > len(self.right):
            if -self.left[0] <= num :
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left,-num)
                l = heapq.heappop(self.left)
                heapq.heappush(self.right, -l)
        else:
            if -self.left[0] >= num :
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right,num)
                r = heapq.heappop(self.right)
                heapq.heappush(self.left, -r)
        
    def findMedian(self) -> float:
        if not self.left and not self.right:
            return 0.0
        if len(self.left) == len(self.right):
            n1 = -self.left[0]
            n2 = self.right[0]
            return (n1+n2)/2
        else:
            return -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        