class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.first = Node(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        cur = self.first.next
        for i in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.first.next
        self.first.next = new
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        cur = self.first
        
        while cur.next:
            cur = cur.next

        new = Node(val)
        cur.next = new
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        cur = self.first
        new = Node(val)
        
        for i in range(index):
            cur = cur.next

        new.next = cur.next
        cur.next = new
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        cur = self.first

        for i in range(index):
            cur = cur.next
        
        deleted_node = cur.next
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