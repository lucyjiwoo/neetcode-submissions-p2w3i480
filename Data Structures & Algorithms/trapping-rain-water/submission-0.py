class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [0]*len(height), [0]*len(height)
        trapped_water = 0
        for i in range(len(height)):
            if i >= 1:
                max_l[i] = max(max_l[i-1], height[i-1])
        for i in reversed(range(len(height))):
            if i < len(height) - 1:
                max_r[i] = max(max_r[i+1], height[i+1])
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            else:
                if max_r[i] > height[i] and max_l[i] > height[i]:
                    trapped_water += min(max_r[i], max_l[i]) - height[i]

        return trapped_water
        



            
