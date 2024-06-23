"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()


        if not root:
            return None

        level = []

        q.append(root)

        while q:
            add = deque()
            level.append([])
            while q:
                node = q.popleft()
                if node:
                    level[-1].append(node)
                    if node.left:
                        add.append(node.left)
                    if node.right:
                        add.append(node.right)
            q = add
            
        # for i in range(len(level)):
        #     print("level")
        #     for j in range(len(level[i])):
        #         print(level[i][j].val)


        for i in range(len(level)):
            for j in range(len(level[i]) - 1):

                level[i][j].next = level[i][j + 1]

        return level[0][0]