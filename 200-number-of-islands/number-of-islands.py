class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        def dfs(r, c):
            if (r,c) in visit:
                return
            elif r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return

            visit.add((r, c))
            if grid[r][c] == "1":
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
            
                return
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit:
                    if grid[i][j] == "1":
                        print("i j")
                        print(i)
                        print(i)
                        c += 1
                        dfs(i, j)
                    else:
                        visit.add((i, j))
        
        return c
