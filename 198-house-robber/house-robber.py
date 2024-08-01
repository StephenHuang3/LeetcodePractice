class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = nums[len(nums) - 1]
        dp[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2])

        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]