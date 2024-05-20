class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        output = [1]

        for i in range(0, len(nums) - 1, 1):
            output.append(cur * nums[i])
            cur = cur * nums[i]

        cur = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * cur
            cur = cur * nums[i]
        
        return output




        