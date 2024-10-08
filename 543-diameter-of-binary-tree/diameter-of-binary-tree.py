# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        if not root:
            return 0
        
        def recur(node, depth):
            # print("node depth", node.val, depth)
            if not node.left and not node.right:
                return depth

            nonlocal max_diameter
            left = recur(node.left, depth + 1) if node.left else 0
            right = recur(node.right, depth + 1) if node.right else 0
            # print("left right", left, right)
            max_diameter = max(max_diameter, left - depth + right - depth)

            return max(left, right)
        
        recur(root, 0)
        return max_diameter