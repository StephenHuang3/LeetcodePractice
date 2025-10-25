class ListNode:
    def __init__(self, count):
        self.c = count
        self.next = None
        self.prev = None
        self.keys = set()

class NodeList:
    def __init__(self):
        self.front = ListNode(0)
        self.end = ListNode(-1)
        self.front.next = self.end
        self.end.prev = self.front
        self.count_to_node = {}
        self.count_to_node[0] = self.front

    def add_node(self, count, prev_node):
        if count in self.count_to_node:
            return

        front_node = prev_node.next

        new = ListNode(count)
        self.count_to_node[count] = new

        prev_node.next = new
        new.prev = prev_node
        new.next = front_node
        front_node.prev = new

    def rmv_node(self, count):
        if count not in self.count_to_node or len(self.count_to_node[count].keys) > 0 or count == 0:
            return

        rmv_node = self.count_to_node[count]
        
        prev_node = rmv_node.prev
        front_node= rmv_node.next
        prev_node.next = front_node
        front_node.prev = prev_node
        del self.count_to_node[count]
        del rmv_node

    def add_val(self, key, count):
        if count not in self.count_to_node:
            raise ValueError("invalid count", count)

        if count == 0:
            return
        
        self.count_to_node[count].keys.add(key)

    def rmv_val(self, key, count):
        if count not in self.count_to_node:
            return
        self.count_to_node[count].keys.discard(key)

class AllOne:

    def __init__(self):
        self.lis = NodeList()
        self.key_to_count = defaultdict(int)

    def inc(self, key: str) -> None:
        new_cnt = self.key_to_count[key] + 1
        self.key_to_count[key] = new_cnt
        self.lis.add_node(new_cnt, self.lis.count_to_node[new_cnt - 1])
        self.lis.add_val(key, new_cnt)
        self.lis.rmv_val(key, new_cnt - 1)
        self.lis.rmv_node(new_cnt - 1)
        

    def dec(self, key: str) -> None:
        new_cnt = self.key_to_count[key] - 1
        self.key_to_count[key] = new_cnt
        self.lis.add_node(new_cnt, self.lis.count_to_node[new_cnt + 1].prev)
        self.lis.add_val(key, new_cnt)
        self.lis.rmv_val(key, new_cnt + 1)
        self.lis.rmv_node(new_cnt + 1)
        

    def getMaxKey(self) -> str:
        if self.lis.front.next == self.lis.end:
            return ""

        return next(
            iter(self.lis.end.prev.keys)
        )
        

    def getMinKey(self) -> str:
        if self.lis.front.next == self.lis.end:
            return ""
        return next(
            iter(self.lis.front.next.keys)
        )


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()