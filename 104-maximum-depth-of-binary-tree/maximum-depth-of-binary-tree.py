# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node: Optional[TreeNode]):
            if not node:
                return 0
            elif node.left and node.right:
                return 1 + max(findDepth(node.left), findDepth(node.right))
            elif node.left:
                return 1 + findDepth(node.left)
            elif node.right:
                return 1 + findDepth(node.right)
            else:
                return 1

        return findDepth(root)
        