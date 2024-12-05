class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        cur = 1
        
        for i in range(len(nums)):
            out[i] = cur
            cur = cur * nums[i]
            
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * cur
            cur = cur * nums[i]

        return out

        