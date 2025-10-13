class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.end = Node(-1,-1, None, None)
        self.front = Node(-1,-1, None, None)
        self.front.prev = self.end
        self.end.next = self.front
        self.hp = {}
        self.size = capacity
        self.cur_len = 0

    def move_front(self,key):
        node = self.hp[key]
        if self.front.prev.key != key:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.front
            node.prev = self.front.prev
            self.front.prev.next = node
            self.front.prev = node

    def del_node(self, key):
        node = self.hp[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.hp[key]

    def get(self, key: int) -> int:
        # print("get", key)
        # print(self.hp)
        if key in self.hp:
            self.move_front(key)
            # print(self.hp)
            # self.print_list()
            return self.hp[key].val
        return -1

    def print_list(self):
        cur = self.end.next
        lis = []
        while cur != self.front:
            lis.append((cur.key, cur.val))
            cur = cur.next
        print(lis)
        

    def put(self, key: int, value: int) -> None:
        # print("put", key)
        # print(self.hp)
        # print("len", self.cur_len)
        if self.cur_len == self.size and  key not in self.hp:
            self.del_node(self.end.next.key)
            self.cur_len -= 1
        if key not in self.hp:
            self.cur_len += 1
        if key in self.hp:
            self.del_node(key)

        new = Node(key, value, self.front.prev, self.front)
        self.hp[key] = new
        self.move_front(key)
        # print(self.hp)
        # self.print_list()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)