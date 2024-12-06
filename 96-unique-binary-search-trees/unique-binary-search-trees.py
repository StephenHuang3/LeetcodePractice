class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (1 + n)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i): # 0 to i - 1
                dp[i] += dp[i - j - 1] * dp[j]

        return dp[n]