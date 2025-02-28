from collections import defaultdict
from bisect import insort


class Allocator:

    def __init__(self, n: int):
        self.free = [(0, n - 1)]
        self.allocations = defaultdict(list)
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        if size > self.n:
            return -1
        for i, (s, e) in enumerate(self.free):
            if e - s + 1 >= size:
                self.allocations[mID].append((s, s + size - 1))
                if e > s + size - 1:
                    self.free[i] = (s + size, e)
                else:
                    self.free.pop(i)
                return s
        return -1

    def freeMemory(self, mID: int) -> int:
        if not self.allocations[mID]:
            return 0
        
        freed = 0
        for s, e in self.allocations.pop(mID):
            insort(self.free, (s, e))
            freed += e - s + 1

        new = [self.free[0]]
        for i, (s, e) in enumerate(self.free[1:]):
            if s <= new[-1][1] + 1:
                new[-1] = (new[-1][0], max(e, new[-1][1]))
            else:
                new.append((s, e))

        self.free = new
        return freed

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)