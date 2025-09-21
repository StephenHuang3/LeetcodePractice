class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        added = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                added += 1
                miss *= 2

        return added