class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or (r,c) in visited:
                return
            
            visited.add((r,c))
            print((r,c))
            if grid[r][c] == "1":
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)
            return

        
        

        for r in range(row):
            for c in range(col):
                
                if (r, c) not in visited and grid[r][c] == "1":
                    print(grid[r][c])
                    count += 1
                    dfs(r, c)

        return count