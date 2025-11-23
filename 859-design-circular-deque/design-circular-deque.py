class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0 for _ in range(k)]
        self.front = 0
        self.end = 0
        self.size = 0
        self.cap = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.cap:
            return False

        if self.size != 0:
            self.front = (self.front - 1) % self.cap
        self.arr[self.front] = value
        self.size += 1

        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size == self.cap:
            return False
        
        if self.size != 0:
            self.end = (self.end + 1) % self.cap
        self.arr[self.end] = value
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        if self.size != 1:
            self.front = (self.front + 1) % self.cap

        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        

        if self.size != 1:
            self.end = (self.end - 1) % self.cap

        self.size -= 1
        return True

    def getFront(self) -> int:
        # print(self.arr)
        # print(self.front)

        if self.size == 0:
            return -1
        return self.arr[self.front]
        

    def getRear(self) -> int:
        print(self.arr)
        print(self.end)
        print(self.size)
        if self.size == 0:
            return -1
        return self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
        
# 0 5

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

5