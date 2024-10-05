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

    def add_node(self, key, val):
        new = ListNode(key, val)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        self.hp[key] = new

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.hp[node.key]
        

    def get(self, key: int) -> int:
        if key not in self.hp:
            return -1
        value = self.hp[key].val
        self.remove_node(self.hp[key])
        self.add_node(key, value)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hp:
            self.remove_node(self.hp[key])
            self.add_node(key, value)
        else:
            if self.used == self.capacity:
                self.remove_node(self.end.prev)
                self.add_node(key, value)
            else:
                self.add_node(key, value)
                self.used += 1

        # if key in self.hp:
        #     self.remove_node(self.hp[key])
        #     self.add_node(key, value)
        # else:
        #     if self.used < self.capacity:
        #         self.used += 1
        #         self.add_node(key, value)
        #     else:
        #         self.add_node(key, value)
        #         self.remove_node(self.end.prev)



        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)