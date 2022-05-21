#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                return nums[i]
            count = 0

        return -1


# @lc code=end
