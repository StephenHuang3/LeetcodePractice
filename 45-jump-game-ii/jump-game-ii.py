class Solution:
    def jump(self, nums: List[int]) -> int:
        farth = 0
        jumps = 0
        end = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            farth = max(farth, i + nums[i])
            if farth >= len(nums) - 1:
                return jumps + 1
            if i == end:
                end = farth
                jumps += 1

        return jumps
