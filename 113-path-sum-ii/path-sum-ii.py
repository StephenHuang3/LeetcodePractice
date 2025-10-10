# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ret = []
        cur_arr = []
        cur_sum = 0

        # if not root.left or not root.right:
        #     if root.val == targetSum:
        #         ret.append([root.val])

        def calc_sum(node):
            nonlocal cur_sum
            cur_sum += node.val
            cur_arr.append(node.val)
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    ret.append(cur_arr.copy())
            if node.left:
                calc_sum(node.left)
            if node.right:
                calc_sum(node.right)
            
            cur_sum -= node.val
            cur_arr.pop()

        calc_sum(root)
        return ret