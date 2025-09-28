class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        seen = set()
        longest = 0
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        R = len(matrix)
        C = len(matrix[0])
        dp = [[-1]*C for i in range(R)]

        def dfs(r, c) -> int:
            if dp[r][c] != -1:
                return dp[r][c]

            best = 1
            best_add = 0
            for dx, dy in dir:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < R and 0 <= nc < C and matrix[r][c] < matrix[nr][nc]:
                    if dp[nr][nc] != -1:
                        best_add = max(best_add, dp[nr][nc])
                    else:
                        best_add = max(best_add, dfs(nr, nc))
            
            dp[r][c] = best + best_add
            return best + best_add

        for r in range(R):
            for c in range(C):
                longest = max(longest, dfs(r, c))

        return longest

            