class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for c in range(C)] for r in range(R)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        # print(dp)

        for r in range(R):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1 

        # print(dp)

        for c in range(C):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1

        # print(dp)

        for r in range(1, R):
            for c in range(1, C):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]