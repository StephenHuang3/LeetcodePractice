# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lis = []

        def dfs(node):
            if not node:
                return
            
            lis.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)



        dfs(root)
        ret = root
        for i in range(1, len(lis)):
            root.left = None
            root.right = lis[i]
            root = root.right
        
        return ret