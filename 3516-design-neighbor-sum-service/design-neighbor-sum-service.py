class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.diag_grid = [[0] * n for _ in range(n)]
        self.horz_vert_grid = [[0] * n for _ in range(n)]
        self.hp = {}

        dir_diag = [(1,1), (-1, -1), (1, -1), (-1, 1)]
        horz_vert = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # print(self.diag_grid)
        # self.diag_grid[0][0] += 1
        # print(self.diag_grid)

        for r in range(n):
            for c in range(n):
                self.hp[grid[r][c]] = (r, c)
                for i in range(4):
                    nr = r + dir_diag[i][0]
                    nc = c + dir_diag[i][1]
                    if 0 <= nr < n and 0 <= nc < n:
                        self.diag_grid[r][c] += grid[nr][nc]
                        # print("diag ", grid[nr][nc], "added to", r, c)
                        # print("diag grid", self.diag_grid)
                    
                    nr = r + horz_vert[i][0]
                    nc = c + horz_vert[i][1]
                    if 0 <= nr < n and 0 <= nc < n:
                        self.horz_vert_grid[r][c] += grid[nr][nc]

        # print(self.diag_grid)
        # print(self.horz_vert_grid)

    def adjacentSum(self, value: int) -> int:
        r, c = self.hp[value]
        return self.horz_vert_grid[r][c]

    def diagonalSum(self, value: int) -> int:
        r, c = self.hp[value]
        return self.diag_grid[r][c]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)