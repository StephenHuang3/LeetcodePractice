class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i in range(len(nums)):
            if target - nums[i] in hp:
                return [hp[target - nums[i]], i]
            hp[nums[i]] = i

