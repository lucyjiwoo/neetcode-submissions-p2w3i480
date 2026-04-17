import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h is bigger than the number of pile or equal
        l, r = 0, max(piles)
        k = r

        while l < r :
            mid = math.ceil((l+r)/2)
            time = 0
            # Calculate time
            for p in piles:
                time += math.ceil(p/mid)
            if time <= h:
                k = mid
                r = mid -1
            else:
                l = mid
        return k