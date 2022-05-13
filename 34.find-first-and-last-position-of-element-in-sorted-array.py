#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min = 0
        max = len(nums) - 1
        while min <= max:
            mid = int((min + max) / 2)

            if nums[mid] == target:
                break
            elif nums[mid] < target:
                min = mid + 1
                continue
            elif nums[mid > target]:
                max = mid + 1
                continue

        if nums[mid] != target:
            return [-1, -1]

        else:
            left, right = mid, mid
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            return [left, right]


# @lc code=end
