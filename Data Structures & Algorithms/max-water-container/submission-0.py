class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 1:
            return 0
        res = (len(heights) - 1) * min(heights[0], heights[-1])
        l, r = 0, len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            res = max(res, w * h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res