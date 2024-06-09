"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hp = {}

        cur = head
        while cur:
            hp[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            hp[cur].next = hp.get(cur.next)
            hp[cur].random = hp.get(cur.random)
            cur = cur.next

        return hp[head]