# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def rob_helper_lis(node_list):
            return sum(rob_helper(node) for node in node_list)

        def rob_helper(node):
            if not node:
                return 0

            if node in cache:
                return cache[node]
            
            grand_children = []
            children = []
            if node.left:
                children.append(node.left)
                l_node = node.left
                if l_node.left:
                    grand_children.append(l_node.left)
                if l_node.right:
                    grand_children.append(l_node.right)
            if node.right:
                children.append(node.right)
                r_node = node.right
                if r_node.left:
                    grand_children.append(r_node.left)
                if r_node.right:
                    grand_children.append(r_node.right)

            ret = max(node.val + rob_helper_lis(grand_children), rob_helper_lis(children))
            cache[node] = ret
            return ret

        return rob_helper(root)

        