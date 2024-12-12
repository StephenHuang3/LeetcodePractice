class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = collections.deque()
        R = len(grid)
        C = len(grid[0])
        steps = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        while q:
            steps += 1
            change = 0
            length = len(q)
            print(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in dir:
                    if 0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        change += 1

            fresh -= change
            if fresh == 0:
                return steps
            if change == 0:
                return -1

        return -1