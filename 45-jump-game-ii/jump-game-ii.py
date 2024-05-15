class Solution:
    def jump(self, nums: List[int]) -> int:
        minjump = [len(nums) for i in range(len(nums))]
        minjump[0] = 0
        for i in range(len(nums)):
            for j in range(1, 1 + nums[i]):
                if i + j >= len(nums):
                    break
                minjump[i + j] = min(minjump[i + j], minjump[i] + 1)

        return minjump[len(nums) - 1]
