from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tuple2row = defaultdict(int)
        matches = 0

        for r in range(n):
            tuple2row[tuple(grid[r])] += 1

        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            if col in tuple2row:
                matches += tuple2row[col]

        return matches