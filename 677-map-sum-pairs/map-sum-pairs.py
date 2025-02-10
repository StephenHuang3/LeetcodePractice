class TrieNode:

    def __init__(self, char):
        self.char = char
        self.total = 0
        self.end = False
        self.val = 0
        self.children = {}


class MapSum:

    def __init__(self):
        self.root = TrieNode('s')
        
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        path = [cur]
        for char in key:
            if char not in cur.children:
                new = TrieNode(char)
                new.char = char
                cur.children[char] = new

            cur = cur.children[char]
            path.append(cur)

        if cur.end:
            diff = val - cur.val
            cur.val = val
            for node in path:
                node.total += diff
        else:
            cur.end = True
            cur.val = val
            for node in path:
                node.total += val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]

        return cur.total

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)