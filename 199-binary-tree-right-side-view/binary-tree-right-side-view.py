# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recur(node, res, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            recur(node.right, res, depth + 1)
            recur(node.left, res, depth + 1)

        res = []
        recur(root, res, 1)
        return res
