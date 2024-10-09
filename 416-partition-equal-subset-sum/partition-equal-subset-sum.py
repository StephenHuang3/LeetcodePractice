class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1: return False
        half, dp = total // 2, 1
        for n in nums:
            dp |= dp << n

        return dp & 1 << half