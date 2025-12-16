class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        num_sum = sum(nums)
        added_len = 0
        k = target // num_sum
        target = target % num_sum
        if target == 0:
            return k * len(nums)

        dp = {0: -1}
        su = 0
        res = inf

        for i, e in enumerate(nums + nums):
            su += e
            if su - target in dp:
                res = min(res, i - dp[su - target])
            dp[su] = i

        return k * len(nums) + res if res < inf else -1

    