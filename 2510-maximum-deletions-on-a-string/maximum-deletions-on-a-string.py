class Solution:
    def deleteString(self, s: str) -> int:
        dp = [1] * len(s)

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, 1 + (len(s) + i) // 2):
                length = j - i
                if s[i:j] == s[j:j + length]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # print(dp)
        return dp[0]


    # when i = 0, j in range(1, 3)