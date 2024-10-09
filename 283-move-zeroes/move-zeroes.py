class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                nums[i - c] = nums[i]


        for i in range(len(nums) - 1, len(nums) - 1 - c, -1):
            nums[i] = 0
            