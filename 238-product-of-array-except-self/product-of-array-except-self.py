class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n
        cur = 1
        
        for i in range(n):
            out[i] = cur
            cur = cur * nums[i]
            
        cur = 1
        for i in range(n - 1, -1, -1):
            out[i] = out[i] * cur
            cur = cur * nums[i]

        return out

