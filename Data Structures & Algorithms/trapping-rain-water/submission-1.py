class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) and O(n)
        # Store left max and right max in two lists.
        # Compare the left and right, and find the smaller value
        # Compare the smaller value with height, if height is equal or bigger, no trap, else h - min of water is trapped

        water = 0
        left,right = [0]*len(height), [0]*len(height)
        for i in range(len(height)):
            j = len(height) - 1 - i
            if i != 0:
                left[i] = max(left[i-1], height[i-1])
                right[j] = max(right[j+1], height[j+1])
                
        for i in range(len(height)):
            min_h = min(left[i],right[i])
            if min_h > height[i]:
                water += min_h - height[i]  
        return water