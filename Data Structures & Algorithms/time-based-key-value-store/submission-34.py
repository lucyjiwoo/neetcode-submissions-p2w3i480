class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, []) + [(value, timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])
        recent = ""
        l, r = 0, len(values)-1
        while l <= r and values[l][1] <= timestamp:
            mid = (l + r) //2
            if values[mid][1] > timestamp:
                r = mid -1
            else:
                recent = values[mid][0]
                l = mid +1
        return recent