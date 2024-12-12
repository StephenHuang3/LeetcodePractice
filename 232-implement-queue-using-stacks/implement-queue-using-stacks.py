class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if len(self.stk2) > 0:
            return self.stk2.pop()
        else:
            for i in range(len(self.stk1)):
                self.stk2.append(self.stk1.pop())
            return self.stk2.pop()

    def peek(self) -> int:
        if len(self.stk2) > 0:
            return self.stk2[-1]
        else:
            for i in range(len(self.stk1)):
                self.stk2.append(self.stk1.pop())
            return self.stk2[-1]
        

    def empty(self) -> bool:
        if len(self.stk1) + len(self.stk2) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()