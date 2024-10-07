from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        directions = [[-1,-1], [-1,0],[0,-1],[1,1], [1,0],[0,1], [1,-1], [-1,1]]
        visited = set((0,0))
        q = deque()
        q.append((0,0))
        depth = 1
        R, C = len(grid), len(grid[0])

        if grid[0][0] + grid[R - 1][C - 1] > 0:
            return -1

        while q:
            # print(q)
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                if r == R - 1 and c == C - 1:
                    return depth
                if grid[r][c] == 0:
                    for dx, dy in directions:
                        nr = r + dx
                        nc = c + dy
                        # print("r c", nr, nc)
                        if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr,nc))
            depth += 1
                
        
        return -1

        