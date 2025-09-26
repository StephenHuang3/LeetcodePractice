from sortedcontainers import SortedDict
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hp = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hp[key][-timestamp] = value # log(n)
        

    def get(self, key: str, timestamp: int) -> str:
        stamps = self.hp[key]

        i = stamps.bisect_left(-timestamp)
        if i < 0 or i == len(stamps):
            return ""
        
        print(i)
        stamp, val = stamps.peekitem(i)
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)