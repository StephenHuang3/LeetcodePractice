# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, cur):
            if not node:
                return int(cur)
            if node.left and node.right:
                return dfs(node.left, cur + str(node.val)) + dfs(node.right, cur + str(node.val))
            elif node.left:
                return dfs(node.left, cur + str(node.val))
            else:
                return dfs(node.right, cur + str(node.val))

        return dfs(root, "")
