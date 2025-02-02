class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            print("R c", r, c)
            visited.add((r, c))
            for dy, dx in dir:
                if 0 <= r + dx < R and 0 <= c + dy < C and grid[r + dx][c + dy] == "1" and (r + dx, c + dy) not in visited:
                    dfs(r + dx, c + dy)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    print("trigger", r, c)
                    dfs(r, c)
                    
        return count
