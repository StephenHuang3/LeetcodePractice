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
        arr = []

        def make_serial(node):
            if not node:
                arr.append(str(1001))
                return
                
            arr.append(str(node.val))
            make_serial(node.left)
            make_serial(node.right)

        make_serial(root)
        # print(arr)
        return ",".join(arr)

    def deserialize(self, data):
        if data == "":
            return None
        
        data = data.split(",")
        c = 0

        def make_node():
            nonlocal c
            int_val = int(data[c])
            c += 1

            if int_val == 1001:
                return None
            new = TreeNode(int_val)
            new.left = make_node()
            new.right = make_node()
            return new

        return make_node()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))