from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(1 << i, i, 0) for i in range(n)]) # (mask, pos, distance)
        visited = set()
        finish_mask = (1 << n) - 1

        while q:
            mask, cur_pos, dist = q.popleft()
            if mask == finish_mask:
                return dist
            for nei in graph[cur_pos]:
                new_mask = mask | 1 << nei
                if (new_mask, nei) not in visited:
                    q.append((new_mask, nei, dist + 1))
                    visited.add((new_mask, nei))