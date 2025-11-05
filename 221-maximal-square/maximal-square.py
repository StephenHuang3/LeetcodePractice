class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for i in range(C)] for j in range(R)]
        
        for c in range(C):
            dp[0][c] = int(matrix[0][c])
        
        for r in range(R):
            dp[r][0] = int(matrix[r][0])

        for r in range(1, R):
            for c in range(1, C):
                if int(matrix[r][c]) == 1:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

        return max(e for row in dp for e in row) ** 2