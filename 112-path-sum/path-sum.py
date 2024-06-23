# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, curval) -> root:
            if not node:
                if curval == targetSum:
                    return True
                else:
                    return False
            if node.left and node.right:
                return dfs(node.right, curval + node.val) or dfs(node.left, curval + node.val)
            elif node.right:
                return dfs(node.right, curval + node.val)
            else:
                return dfs(node.left, curval + node.val)

        return dfs(root, 0)

        