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

        cur = head
        hp = {}

        while cur:
            hp[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head

        while cur:
            hp[cur].random = hp.get(cur.random)
            hp[cur].next = hp.get(cur.next)
            cur = cur.next

        return hp[head]
