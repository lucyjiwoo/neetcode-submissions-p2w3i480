class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # store index order decreaing of nums[i]
        l, r = 0,0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # range check
            if q[0] < l:
                q.popleft()
            if r-l + 1 == k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output