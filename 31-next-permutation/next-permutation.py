class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peak = 0
        peak_idx = 0
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1 and nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                return
            if i == 0:
                return nums.reverse()
            if nums[i-1] < nums[i]:
                peak = nums[i]
                peak_idx = i
                break

        peak_left = nums[i-1]
        right_min = peak
        right_idx = peak_idx
        for i in range(peak_idx, len(nums)):
            if nums[i] < right_min and nums[i] > peak_left:
                right_min = nums[i]
                right_idx = i
        
        nums[right_idx], nums[peak_idx - 1] = nums[peak_idx - 1], nums[right_idx]

        nums[peak_idx:] = sorted(nums[peak_idx:])