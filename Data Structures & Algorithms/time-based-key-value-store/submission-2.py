from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or self.data[key][0][0] > timestamp:
            return ''

        l, r = 0, len(self.data[key]) - 1
        print(f'Timestamp: {timestamp}')
        while l <= r:
            mid = l + (r - l) // 2
            if self.data[key][mid][0] > timestamp:
                r = mid - 1
            elif self.data[key][mid][0] < timestamp:
                l = mid + 1
            else:
                return self.data[key][mid][1]
            print(mid)
        return self.data[key][mid][1] if self.data[key][mid][0] < timestamp else self.data[key][mid-1][1]
