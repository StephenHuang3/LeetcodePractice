# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        ret = []

        def dfs(node):
            if not node:
                ret.append("N")
                return
            ret.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(ret)
        return ",".join(ret)

        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if len(data) == 0:
            return None
        
        data = data.split(",")       

        pos = [0]
        def create():
            if data[pos[0]] == "N":
                pos[0] += 1
                return None
            new = TreeNode(data[pos[0]])
            pos[0] += 1
            new.left = create()
            new.right = create()
            return new

        return create()
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))