# Definition for double-linked list.
class ListNode:
    def __init__(self, key = 0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.used = 0
        self.capacity = capacity
        self.hp = {}
        self.head = ListNode(-1, -1)
        self.end = ListNode(-1, -1)
        self.head.next = self.end
        self.end.prev = self.head

    def addNode(self, key, val):
        new = ListNode(key, val)
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new
        self.hp[key] = new
    def rmNode(self, node: ListNode):
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.hp[node.key]


    def get(self, key: int) -> int:
        if key in self.hp:
            val = self.hp[key].val
            self.rmNode(self.hp[key])
            self.addNode(key, val)
            return val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hp:
            self.rmNode(self.hp[key])
            self.addNode(key, value)
        else:
            if self.used < self.capacity:
                self.used += 1
                self.addNode(key, value)
            else:
                self.addNode(key, value)
                self.rmNode(self.end.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)