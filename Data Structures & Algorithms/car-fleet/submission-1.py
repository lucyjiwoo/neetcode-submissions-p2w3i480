class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Edge Case: No car or only one car
        if len(position) <= 1:
            return len(position)

        # need to sort the order based on position
        pair = [[position[i], speed[i]] for i in range(len(speed))]
        pair.sort()         # O(nlogn)

        res = 0
        while pair:
            time = (target - pair[-1][0])/pair[-1][1]
            pair.pop()
            while pair and pair[-1][0] + pair[-1][1] * time >= target:
                pair.pop()
            res += 1
        return res


