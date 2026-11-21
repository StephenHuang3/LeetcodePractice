from collections import deque
from copy import deepcopy

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        ancestors = defaultdict(deque)
        ancestors[0].append(-1)
        dir_graph = defaultdict(list)
        new_parent = deepcopy(parent)
        new_dir_graph = defaultdict(list)
        output = [0 for i in range(len(parent))]

        for i in range(len(parent)):
            dir_graph[parent[i]].append(i)

        def dfs(cur):
            if s[cur] in ancestors and len(ancestors[s[cur]]) > 0:
                new_parent[cur] = ancestors[s[cur]][-1]
            ancestors[s[cur]].append(cur)
            for child in dir_graph[cur]:
                dfs(child)
            ancestors[s[cur]].pop()

        dfs(0)

        print(new_parent)
        for i in range(len(parent)):
            new_dir_graph[new_parent[i]].append(i)

        def fill_size(cur):
            total = 1
            for child in new_dir_graph[cur]:
                total += fill_size(child)

            output[cur] = total
            return total
        
        fill_size(0)

        return output