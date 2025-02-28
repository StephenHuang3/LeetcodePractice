class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.mem[i] == 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == size:
                for j in range(i, i - size, -1):
                    self.mem[j] = mID
                return i - size + 1

        return -1
        

    def freeMemory(self, mID: int) -> int:
        c = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = 0
                c += 1
        return c


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)