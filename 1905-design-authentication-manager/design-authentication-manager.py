from collections import deque

class HPList:
    def __init__(self):
        self.front = ListNode('z', 0)
        self.end = ListNode('z', 0)
        self.front.next = self.end
        self.end.prev = self.front
        self.size = 0
        self.hp = {}

    def print_list(self):
        cur = self.front.next
        ret = []

        while cur != self.end:
            ret.append((cur.expire, cur.token))
            cur = cur.next

        print(ret)

    def add_back(self, token, expire):
        new = ListNode(token, expire)
        self.hp[token] = new
        new.prev = self.end.prev
        new.next = self.end
        self.end.prev.next = new
        self.end.prev = new
        self.size += 1

    def rmv(self, token):
        if token not in self.hp:
            return
        rmv_node = self.hp[token]
        rmv_prev = rmv_node.prev
        rmv_next = rmv_node.next
        rmv_prev.next = rmv_next
        rmv_next.prev = rmv_prev
        self.size -= 1
        del self.hp[token]

    def rmv_expired(self, cur_time):
        cur = self.front.next
        while cur != self.end and cur.expire <= cur_time:
            nxt = cur.next
            self.rmv(cur.token)
            cur = nxt

    def extend_time(self, token, new_time):
        self.rmv(token)
        self.add_back(token, new_time)


class ListNode:
    def __init__(self, token, expire):
        self.token = token
        self.next = None
        self.prev = None
        self.expire = expire


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.cur_live = deque()
        self.lis = HPList()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.lis.rmv_expired(currentTime)
        self.lis.add_back(tokenId, currentTime + self.ttl)
        # print("size after gen", self.lis.size)
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.lis.rmv_expired(currentTime)
        if tokenId not in self.lis.hp:
            return
        self.lis.extend_time(tokenId, currentTime + self.ttl)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # print("before rmv")
        # print(currentTime)
        # self.lis.print_list()
        self.lis.rmv_expired(currentTime)
        # self.lis.print_list()
        # print("cur size", self.lis.size)
        return self.lis.size
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)