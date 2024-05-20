class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = nums[0]
        output = [1 for i in range(len(nums))]

        for i in range(1, len(nums), 1):
            output[i] *= cur
            cur *= nums[i]

        cur = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= cur
            cur *= nums[i]

        print(output)
        return output




        