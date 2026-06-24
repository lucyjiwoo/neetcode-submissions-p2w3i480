class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)% groupSize != 0:
            return False
        
        count  = Counter(hand)
        q = list(count.keys())
        heapq.heapify(q)

        while q:
            start = q[0]
            for card in range(start, start + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1

                if count[card] == 0:
                    if card == q[0]:
                        heapq.heappop(q)
                    else:
                        return False
        
        return True


