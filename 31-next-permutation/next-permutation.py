class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        peak = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                peak = i
                break

        if peak == -1:
            nums.reverse()
            return
        
        minval = float('infinity')
        minvalidx = -1
        for i in range(len(nums) - 1, peak - 1, -1):
            if nums[i] < minval and nums[i] > nums[peak - 1]:
                minvalidx = i
                minval = nums[i]

        nums[peak - 1], nums[minvalidx] = nums[minvalidx], nums[peak - 1]

        nums[peak:] = sorted(nums[peak:])
        return