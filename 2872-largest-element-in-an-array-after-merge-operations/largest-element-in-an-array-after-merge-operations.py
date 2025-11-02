class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        max_found = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= max_found:
                max_found += nums[i]
            else:
                max_found = nums[i]

        return max_found