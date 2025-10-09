# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return

        idx = {v: i for i, v in enumerate(inorder)}
        n = len(preorder)
        self.p = 0

        def helper(lo: int, hi: int) -> Optional['TreeNode']:
            if lo > hi:
                return None

            root_val = preorder[self.p]
            new = TreeNode(root_val)
            self.p += 1

            mid = idx[root_val]
            new.left = helper(lo, mid - 1)
            new.right = helper(mid + 1, hi)
            return new

        return helper(0, n - 1)