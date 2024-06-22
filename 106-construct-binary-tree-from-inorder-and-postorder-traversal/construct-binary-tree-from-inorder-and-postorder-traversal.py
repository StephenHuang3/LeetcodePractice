# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        # print("mid")
        # print(mid)

        # print("inorder")
        # print(len(inorder[mid + 1:]))
        # print(len(inorder[:mid]))

        # print('postorder')
        # print(len(postorder[:mid + 1]))
        # print(len(postorder[mid: -1]))

        root.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        
        return root