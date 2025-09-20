class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        found = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    found.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1

        return list(found)
