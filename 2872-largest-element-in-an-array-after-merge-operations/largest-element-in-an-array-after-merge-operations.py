class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        max_found = nums[-1]
        while len(nums) > 1:
            max_found = max(max_found, nums[-1])
            if nums[-2] <= nums[-1]:
                popped = nums.pop()
                nums[-1] += popped
            else:
                nums.pop()

        return max(max_found, nums[0])