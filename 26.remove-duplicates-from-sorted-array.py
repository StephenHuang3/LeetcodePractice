#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums) - 1):
            if nums[count] == nums[count + 1]:
                nums.pop(count + 1)
            else:
                count += 1

        return len(nums)


# @lc code=end
