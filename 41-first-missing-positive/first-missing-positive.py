class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contain1 = False
        def negate(x):
            if x > 0:
                return -x
            return x

        for i in range(len(nums)):
            if nums[i] == 1:
                contain1 = True
            if nums[i] <= 0:
                nums[i] = 1

        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                nums[abs(nums[i]) - 1] = negate(nums[abs(nums[i]) - 1])

        print(nums)

        if not contain1:
            return 1

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1