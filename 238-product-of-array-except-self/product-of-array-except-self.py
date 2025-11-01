class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        cur = 1
        
        for i in range(len(nums) - 2, -1, -1):
            cur = nums[i + 1] * cur
            prefix[i] *= cur

        return prefix