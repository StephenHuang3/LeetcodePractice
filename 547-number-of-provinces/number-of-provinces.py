class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        rank = [1] * N
        parent = [i for i in range(N)]
        num_prov = N

        def find_par(prov):
            res = prov

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        
        def union(prov1, prov2):
            parent1 = find_par(prov1)
            parent2 = find_par(prov2)

            if parent1 == parent2:
                return 0

            if rank[parent1] > rank[parent2]:
                rank[parent1] += rank[parent2]
                parent[parent2] = parent1
                parent[prov2] = parent1
            else:
                rank[parent2] += rank[parent1]
                parent[parent1] = parent2
                parent[prov1] = parent2
            
            return 1

        for i in range(N):
            for j in range(i + 1, N, 1):
                if isConnected[i][j] == 1:
                    num_prov -= union(i, j)

        return num_prov