# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def recur(node, low_possible, high_possible):
            nonlocal total
            if low <= node.val <= high:
                total += node.val
            
            if node.left:
                if low <= node.val:
                    recur(node.left, low_possible, node.val)
            if node.right:
                if node.val <= high:
                    recur(node.right, node.val, high_possible)

        recur(root, float("-infinity"), float("infinity"))
        return total
