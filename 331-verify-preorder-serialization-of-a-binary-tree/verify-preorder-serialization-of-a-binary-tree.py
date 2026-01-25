class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        parents = []
        at_left = True
        stk = []

        if (len(nodes) > 1 and nodes[0] == "#") or (len(nodes) <= 2 and nodes[0] != "#"):
            return False

        if nodes[0] == "#" and len(nodes) == 1:
            return True

        parents.append(nodes[0])

        for node in nodes[1:]:
            if not parents:
                return False
            if node == "#":
                if at_left:
                    at_left = False
                else:
                    parents.pop()
                    while stk:
                        popped = stk.pop()
                        if popped:
                            break
                        else:
                            parents.pop()
                    at_left = False
            else:
                parents.append(node)
                stk.append(at_left)
                at_left = True
            
        if not parents:
            return True
        return False

        
        # stk: 
        # at_left: f