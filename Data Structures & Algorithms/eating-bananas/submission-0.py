import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h is bigger than the number of pile or equal

        k = piles[0]
        for pile in piles:
            k = max(k, pile)
        if len(piles) == h:
            return k
        mid = k // 2
        while mid < k and mid > 0:
            k_h = 0
            for pile in piles:
                k_h += math.ceil(pile/mid)
            if k_h <= h:
                k = mid
                mid = k //2
            else:
                mid = (mid + k + 1)//2
        return k 