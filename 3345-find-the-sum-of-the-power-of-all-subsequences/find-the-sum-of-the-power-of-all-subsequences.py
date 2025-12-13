MOD = 10**9 + 7


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        dp = [1] + [0] * k
        for a in nums:
            for v in range(k, -1, -1):
                dp[v] = (dp[v] * 2 + (dp[v - a] if v >= a else 0)) % mod
        return dp[k]

        # print(dp)
        return dp[k][-1]
