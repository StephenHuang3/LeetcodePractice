"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        have = {}
        def clone(node):
            if node in have:
                return have[node]

            new = Node()
            new.val = node.val
            have[node] = new
            for nei in node.neighbors:
                new.neighbors.append(clone(nei))

            return new

        return clone(node)
        