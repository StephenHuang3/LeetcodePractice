class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0

        for i in range(len(nums)):
            if dis < i:
                return False
            dis = max(dis, i + nums[i])

        if dis >= len(nums) - 1:
            return True
        else:
            return False

        