class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Input list of tasks : tasks and number: n
        # highest freq is priority
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]      # Fast forward to next q time
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

