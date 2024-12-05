class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
            return 0
        
        par = [i for i in range(len(isConnected))]
        size = [1 for i in range(len(isConnected))]

        provinces = len(isConnected)

        def getParent(c):
            while par[c] != par[par[c]]:
                par[c] = par[par[c]]

            return par[c]

        def union(c1, c2):
            p1 = getParent(c1)
            p2 = getParent(c2)

            if p1 == p2:
                return 0

            if size[c1] < size[c2]:
                par[p1] = p2
                size[p2] += size[p1]
            else:
                par[p2] = p1
                size[p1] += size[p2]

            return 1

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if r == c:
                    continue
                if isConnected[r][c]:
                    # print("r c", r, c)
                    provinces -= union(r, c)

        return max(1, provinces)
