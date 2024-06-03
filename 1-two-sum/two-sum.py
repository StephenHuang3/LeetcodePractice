class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i, n in enumerate(nums):
            if n in hp:
                return [i, hp[n]]
            hp[target - n] = i

        


        