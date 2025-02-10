class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.first = Node(0)
        self.last = Node(0)
        self.first.next = self.last
        self.last.prev = self.first
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        mid = self.length // 2

        if index <= mid:
            cur = self.first.next
            for i in range(index):
                cur = cur.next
        else:
            cur = self.last.prev
            for i in range(self.length - index - 1):
                cur = cur.prev

        return cur.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.first.next
        new.prev = self.first
        self.first.next.prev = new
        self.first.next = new
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.next = self.last
        new.prev = self.last.prev
        self.last.prev.next = new
        self.last.prev = new
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        new = Node(val)
        mid = self.length // 2

        if index <= mid:
            cur = self.first
            for i in range(index):
                cur = cur.next
        else:
            cur = self.last
            for i in range(self.length - index + 1):
                cur = cur.prev

        new.next = cur.next
        new.prev = cur
        cur.next.prev = new
        cur.next = new
        self.length += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        mid = self.length // 2
        
        if index <= mid:
            cur = self.first
            for i in range(index):
                cur = cur.next
        else:
            cur = self.last
            for i in range(self.length - index + 1):
                cur = cur.prev
        
        deleted_node = cur.next
        deleted_node.next.prev = cur
        cur.next = deleted_node.next
        del deleted_node
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)