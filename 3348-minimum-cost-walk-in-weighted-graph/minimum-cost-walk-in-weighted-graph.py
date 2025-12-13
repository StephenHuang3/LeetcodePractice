from collections import defaultdict


class Unionfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def union(self, a, b):
        a_parent = self.find_parent(a)
        b_parent = self.find_parent(b)

        if a_parent == b_parent:
            return

        if self.size[a_parent] < self.size[b_parent]:
            self.size[b_parent] += self.size[a_parent]
            self.parent[a_parent] = b_parent
        else:
            self.size[a_parent] += self.size[b_parent]
            self.parent[b_parent] = a_parent

    def find_parent(self, a):
        while self.parent[a] != self.parent[self.parent[a]]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]

        return self.parent[a]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = Unionfind(n)
        for a, b, val in edges:
            uf.union(a, b)

        root2edges = defaultdict(list)
        root2walk = {}
        ret = []

        for a, b, val in edges:
            root2edges[uf.find_parent(a)].append(val)

        for parent, edges in root2edges.items():
            cur = edges[0]
            for i in range(1, len(edges)):
                cur = cur & edges[i]

            root2walk[parent] = cur

        for a, b in query:
            a_parent = uf.find_parent(a)
            b_parent = uf.find_parent(b)
            if a_parent != b_parent:
                ret.append(-1)
            else:
                ret.append(root2walk[a_parent])

        return ret

            